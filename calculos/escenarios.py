from calculos.interes import (
    interes_simple,
    interes_compuesto,
    interes_compuesto_con_aportes
)


def generar_escenarios(
    capital,
    tasa,
    aporte
):

    escenarios = []

    for años in [1, 5, 10, 15, 20]:

        simple = interes_simple(
            capital,
            tasa,
            años
        )

        if aporte > 0:

            compuesto = interes_compuesto_con_aportes(
                capital,
                tasa,
                años,
                aporte
            )

        else:

            compuesto = interes_compuesto(
                capital,
                tasa,
                años
            )

        escenarios.append(

            (
                años,
                simple,
                compuesto
            )

        )

    return escenarios