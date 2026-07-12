def calcular_puntaje(
    tasa,
    tiempo,
    aporte,
    inflacion,
    riesgo
):

    puntaje = 50

    if tasa >= 0.08:
        puntaje += 10

    if tiempo >= 10:
        puntaje += 20

    if aporte > 0:
        puntaje += 10

    if inflacion < 5:
        puntaje += 5

    if "Bajo" in riesgo:
        puntaje += 10

    if "Alto" in riesgo:
        puntaje -= 20

    if puntaje > 100:
        puntaje = 100

    if puntaje >= 85:

        estado = "🟢 Excelente"

    elif puntaje >= 70:

        estado = "🟡 Buena"

    else:

        estado = "🔴 Riesgosa"

    return puntaje, estado