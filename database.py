import sqlite3


DATABASE = "simulador.db"


def conectar():

    return sqlite3.connect(DATABASE)


def crear_tabla():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS simulaciones(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            capital REAL,

            tasa REAL,

            tiempo REAL,

            tipo TEXT,

            capital_final REAL,

            ganancia REAL

        )

    """)

    conexion.commit()

    conexion.close()

def guardar_simulacion(

    capital,
    tasa,
    tiempo,
    tipo,
    capital_final,
    ganancia

):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        INSERT INTO simulaciones(

            capital,
            tasa,
            tiempo,
            tipo,
            capital_final,
            ganancia

        )

        VALUES(?,?,?,?,?,?)

    """,

    (

        capital,
        tasa,
        tiempo,
        tipo,
        capital_final,
        ganancia

    )

    )

    conexion.commit()

    conexion.close()

def obtener_simulaciones():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        SELECT

            id,
            capital,
            tasa,
            tiempo,
            tipo,
            capital_final,
            ganancia

        FROM simulaciones

        ORDER BY id DESC

    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos

def obtener_estadisticas():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM simulaciones
    """)

    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT AVG(ganancia)
        FROM simulaciones
    """)

    promedio = cursor.fetchone()[0]

    cursor.execute("""
        SELECT MAX(capital_final)
        FROM simulaciones
    """)

    mayor = cursor.fetchone()[0]

    cursor.execute("""
        SELECT tipo, COUNT(*)
        FROM simulaciones
        GROUP BY tipo
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    resultado = cursor.fetchone()

    conexion.close()

    return {

        "total": total,

        "promedio": promedio if promedio else 0,

        "mayor": mayor if mayor else 0,

        "tipo": resultado[0] if resultado else "Sin datos"

    }


def eliminar_simulacion(id_simulacion):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        DELETE FROM simulaciones

        WHERE id = ?

    """, (id_simulacion,))

    conexion.commit()

    conexion.close()


def vaciar_historial():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        DELETE FROM simulaciones

    """)

    conexion.commit()

    conexion.close()



def obtener_dashboard():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""

    SELECT

    COUNT(*),

    AVG(capital),

    AVG(ganancia),

    MAX(ganancia),

    SUM(capital)

    FROM simulaciones

    """)

    datos = cursor.fetchone()

    conexion.close()

    return datos



def interes_favorito():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""

    SELECT tipo,

    COUNT(*)

    FROM simulaciones

    GROUP BY tipo

    ORDER BY COUNT(*) DESC

    LIMIT 1

    """)

    dato = cursor.fetchone()

    conexion.close()

    if dato:
        return dato[0]

    return "Sin datos"




def obtener_historial_dashboard():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""

        SELECT
            id,
            capital_final

        FROM simulaciones

        ORDER BY id

    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos



def obtener_simulacion(id_simulacion):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        SELECT *

        FROM simulaciones

        WHERE id = ?

    """, (id_simulacion,))

    dato = cursor.fetchone()

    conexion.close()

    return dato