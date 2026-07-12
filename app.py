from flask import Flask, render_template, request, redirect, send_file
from sympy import latex as sympy_latex
from calculos.interes import interes_simple, interes_compuesto, interes_compuesto_con_aportes, ganancia
from calculos.derivadas import derivada_simple, derivada_compuesta, evaluar_derivada
from calculos.graficos import grafico_crecimiento
from calculos.limites import limite_simple, limite_compuesto
from database import crear_tabla, guardar_simulacion, obtener_simulaciones, obtener_estadisticas, eliminar_simulacion, vaciar_historial, obtener_dashboard, interes_favorito, obtener_historial_dashboard, obtener_simulacion
from calculos.inflacion import capital_real
from calculos.analisis import generar_analisis
from calculos.comparacion import grafico_comparacion
from calculos.meta import ahorro_mensual
from calculos.dashboard import grafico_dashboard
from calculos.riesgo import evaluar_riesgo
from calculos.recomendacion import generar_recomendaciones
from calculos.puntaje import calcular_puntaje
from calculos.escenarios import generar_escenarios
from calculos.frecuencia import comparar_frecuencias
from utils.pdf import crear_pdf

app = Flask(__name__)
crear_tabla()


@app.template_filter("limpio")
def limpio(valor):
    """
    Muestra un número sin decimales innecesarios: 10.0 -> "10", 2.5 -> "2.5".
    """
    valor = float(valor)
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:g}"


@app.route("/")
def inicio():
    datos = obtener_dashboard()
    favorito = interes_favorito()
    ultimas = obtener_simulaciones()[:5]
    historial = obtener_historial_dashboard()
    grafico = grafico_dashboard(historial)
    return render_template(
        "index.html",
        datos=datos,
        favorito=favorito,
        ultimas=ultimas,
        grafico=grafico
    )


@app.route("/simulador")
def simulador():
    return render_template("simulador.html")


@app.route("/historial")
def historial():
    simulaciones = obtener_simulaciones()
    return render_template(
        "historial.html",
        simulaciones=simulaciones
    )

@app.route("/eliminar/<int:id>")
def eliminar(id):
    eliminar_simulacion(id)
    return redirect("/historial")

@app.route("/vaciar")
def vaciar():
    vaciar_historial()
    return redirect("/historial")


@app.route("/resultado", methods=["POST"])
def resultado():
    capital = float(request.form["capital"])
    tasa = float(request.form["tasa"]) / 100
    tiempo = float(request.form["tiempo"])
    tipo = request.form["tipo"]
    aporte = float(request.form["aporte"])
    inflacion = float(request.form["inflacion"])
    frecuencia = int(request.form.get("frecuencia", 1))


    capital_simple = interes_simple(capital, tasa, tiempo)
    ganancia_simple = ganancia(capital, capital_simple)
    if aporte > 0:
        capital_compuesto = interes_compuesto_con_aportes(capital, tasa, tiempo, aporte)
    else:
        capital_compuesto = interes_compuesto(capital, tasa, tiempo, frecuencia)
    ganancia_compuesta = ganancia(capital, capital_compuesto)
    diferencia = capital_compuesto - capital_simple
    if capital_simple != 0:
        porcentaje_mejora = (diferencia / capital_simple) * 100
    else:
        porcentaje_mejora = 0

    if tipo == "simple":
        capital_final = interes_simple(capital, tasa, tiempo)
        derivada = derivada_simple(capital, tasa)
        limite = limite_simple(capital, tasa)
        comparacion_frecuencias = None
    else:
        if aporte > 0:
            capital_final = interes_compuesto_con_aportes(capital, tasa, tiempo, aporte)
            derivada = derivada_compuesta(capital, tasa)
            limite = limite_compuesto(capital, tasa)
        else:
            capital_final = interes_compuesto(capital, tasa, tiempo, frecuencia)
            derivada = derivada_compuesta(capital, tasa, frecuencia)
            limite = limite_compuesto(capital, tasa, frecuencia)
        comparacion_frecuencias = comparar_frecuencias(capital, tasa, tiempo)
    interes_ganado = ganancia(capital, capital_final)
    capital_ajustado = capital_real(capital_final, inflacion, tiempo)
    velocidad = evaluar_derivada(derivada, tiempo)
    derivada_latex = sympy_latex(derivada.evalf(6), mul_symbol="dot")
    limite_latex = sympy_latex(limite.evalf(6), mul_symbol="dot")
    escenarios = generar_escenarios(capital, tasa, aporte)
    riesgo, descripcion_riesgo = evaluar_riesgo(tasa, tiempo)
    recomendaciones = generar_recomendaciones(tipo, tasa, tiempo, aporte, inflacion, riesgo)
    puntaje, estado = calcular_puntaje(tasa, tiempo, aporte, inflacion, riesgo)
    grafico = grafico_crecimiento(capital, tasa, tiempo, tipo, frecuencia, aporte)
    grafico_comparativo = grafico_comparacion(capital, tasa, tiempo, aporte)
    analisis = generar_analisis(capital, capital_final, capital_ajustado, tasa, tiempo, aporte, tipo
                                )
    guardar_simulacion(capital, tasa, tiempo, tipo, capital_final, interes_ganado)

    return render_template(
        "resultados.html",
        capital=capital,
        tasa=tasa*100,
        tiempo=tiempo,
        tipo=tipo,
        capital_final=capital_final,
        interes_ganado=interes_ganado,
        derivada_latex=derivada_latex,
        velocidad=velocidad,
        grafico=grafico,
        limite_latex=limite_latex,
        capital_ajustado=capital_ajustado,
        inflacion=inflacion,
        aporte=aporte,
        frecuencia=frecuencia,
        comparacion_frecuencias=comparacion_frecuencias,
        analisis=analisis,
        capital_simple=capital_simple,
        capital_compuesto=capital_compuesto,
        ganancia_simple=ganancia_simple,
        ganancia_compuesta=ganancia_compuesta,
        diferencia=diferencia,
        porcentaje_mejora=porcentaje_mejora,
        grafico_comparativo=grafico_comparativo,
        riesgo=riesgo,
        descripcion_riesgo=descripcion_riesgo,
        recomendaciones=recomendaciones,
        puntaje=puntaje,
        estado=estado,
        escenarios=escenarios,
        )






@app.route("/educacion")
def educacion():
    return render_template("educacion.html")



@app.route("/meta", methods=["GET", "POST"])
def meta():

    if request.method == "POST":

        capital = float(request.form["capital"])
        objetivo = float(request.form["meta"])
        tasa = float(request.form["tasa"]) / 100
        tiempo = float(request.form["tiempo"])

        ahorro = ahorro_mensual(
            objetivo,
            capital,
            tasa,
            tiempo
        )

        return render_template(
            "meta.html",
            ahorro=ahorro,
            capital=capital,
            objetivo=objetivo,
            tasa=tasa * 100,
            tiempo=tiempo
        )

    return render_template(
        "meta.html",
        ahorro=None
    )

@app.route("/pdf/<int:id>")
def pdf(id):

    simulacion = obtener_simulacion(id)

    archivo = f"static/reporte_{id}.pdf"

    crear_pdf(
        simulacion,
        archivo
    )

    return send_file(
        archivo,
        as_attachment=True
    )


@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)