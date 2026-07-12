from calculos.interes import interes_compuesto


FRECUENCIAS = [
    ("Anual", 1),
    ("Semestral", 2),
    ("Trimestral", 4),
    ("Mensual", 12),
]


def comparar_frecuencias(capital, tasa, tiempo):
    """
    Compara el capital final con la misma tasa y tiempo, capitalizando
    con distinta frecuencia. Responde: ¿cuánto importa capitalizar
    más seguido?
    """

    resultados = []

    for nombre, frecuencia in FRECUENCIAS:

        capital_final = interes_compuesto(capital, tasa, tiempo, frecuencia)

        resultados.append((nombre, frecuencia, capital_final))

    return resultados
