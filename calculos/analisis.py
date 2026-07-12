def generar_analisis(
    capital,
    capital_final,
    capital_real,
    tasa,
    tiempo,
    aporte,
    tipo
):

    mensajes = []

    if tipo == "compuesto":
        mensajes.append(
            "El interés compuesto aprovecha la capitalización de los intereses, permitiendo un crecimiento acelerado del capital."
        )
    else:
        mensajes.append(
            "El interés simple genera un crecimiento lineal, por lo que la rentabilidad aumenta de forma constante."
        )

    if tiempo >= 10:
        mensajes.append(
            "El horizonte de inversión es largo, lo que favorece significativamente el crecimiento del capital."
        )

    elif tiempo >= 5:
        mensajes.append(
            "El plazo es adecuado para observar un crecimiento importante de la inversión."
        )

    else:
        mensajes.append(
            "El plazo es corto. Un mayor tiempo podría aumentar considerablemente la rentabilidad."
        )

    if aporte > 0:
        mensajes.append(
            "Realizar aportes periódicos incrementa considerablemente el capital acumulado."
        )

    diferencia = capital_final - capital_real

    if diferencia > capital * 0.10:

        mensajes.append(
            "La inflación reduce de manera importante el poder adquisitivo del capital obtenido."
        )

    return mensajes