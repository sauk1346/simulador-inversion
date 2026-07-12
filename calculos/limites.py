from sympy import symbols, limit, oo

t = symbols("t")


def limite_simple(capital, tasa):

    funcion = capital * (1 + tasa * t)

    return limit(funcion, t, oo)


def limite_compuesto(capital, tasa, frecuencia=1):

    funcion = capital * ((1 + tasa / frecuencia) ** (frecuencia * t))

    return limit(funcion, t, oo)