def evaluar_riesgo(tasa, tiempo):

    tasa = tasa * 100

    if tasa < 5 and tiempo < 3:
        return (
            "🟢 Riesgo Bajo",
            "La inversión es conservadora y presenta poca volatilidad."
        )

    elif tasa < 10 and tiempo < 8:
        return (
            "🟡 Riesgo Medio",
            "Existe un equilibrio entre rentabilidad y riesgo."
        )

    else:
        return (
            "🔴 Riesgo Alto",
            "La inversión puede generar mayor rentabilidad, pero también implica un mayor riesgo."
        )