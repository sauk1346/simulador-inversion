"""
Funciones relacionadas con el cálculo de intereses.
"""

def interes_simple(capital, tasa, tiempo):
    """
    Calcula el capital final usando interés simple.

    Fórmula:
    C = C0 * (1 + r*t)
    """

    return capital * (1 + tasa * tiempo)


def interes_compuesto(capital, tasa, tiempo, frecuencia=1):
    """
    Calcula el capital final usando interés compuesto.

    frecuencia = veces que se capitaliza el interés por año
    (1 = anual, 2 = semestral, 4 = trimestral, 12 = mensual).

    Fórmula:
    C = C0 * (1 + r/n)^(n*t)
    """

    return capital * ((1 + tasa / frecuencia) ** (frecuencia * tiempo))


def ganancia(capital_inicial, capital_final):
    """
    Retorna la ganancia obtenida.
    """

    return capital_final - capital_inicial


def interes_compuesto_con_aportes(
    capital,
    tasa,
    tiempo,
    aporte
):

    monto = capital

    meses = int(tiempo * 12)

    tasa_mensual = tasa / 12

    for _ in range(meses):

        monto *= (1 + tasa_mensual)

        monto += aporte

    return monto