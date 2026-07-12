def ahorro_mensual(meta, capital, tasa_anual, años):
    
    tasa_mensual = tasa_anual / 12
    meses = años * 12

    if tasa_mensual == 0:
        return (meta - capital) / meses

    capital_futuro = capital * (1 + tasa_mensual) ** meses

    aporte = (
        meta - capital_futuro
    ) * tasa_mensual / (
        (1 + tasa_mensual) ** meses - 1
    )

    return max(aporte, 0)