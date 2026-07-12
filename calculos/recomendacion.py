def generar_recomendaciones(tipo, tasa, tiempo, aporte, inflacion, riesgo):

    recomendaciones = []

    if tipo == "simple":
        recomendaciones.append(
            "El interés simple es recomendable para inversiones de corto plazo."
        )
    else:
        recomendaciones.append(
            "El interés compuesto aprovecha el efecto de capitalización y suele ser más conveniente."
        )

    if tiempo >= 10:
        recomendaciones.append(
            "El plazo es suficientemente largo para obtener un crecimiento importante."
        )
    elif tiempo < 3:
        recomendaciones.append(
            "En períodos cortos las ganancias serán menores."
        )

    if aporte > 0:
        recomendaciones.append(
            "Realizar aportes periódicos acelera el crecimiento del capital."
        )

    if inflacion >= 6:
        recomendaciones.append(
            "La inflación es elevada. Conviene invertir para no perder poder adquisitivo."
        )

    if "Alto" in riesgo:
        recomendaciones.append(
            "Esta inversión presenta un riesgo considerable. Analiza si se ajusta a tu perfil."
        )

    return recomendaciones