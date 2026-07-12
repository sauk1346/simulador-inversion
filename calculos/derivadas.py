from sympy import symbols, diff, N

# Variable independiente
t = symbols("t")


def derivada_simple(capital, tasa):
    """
    Derivada del interés simple
    C(t)=C0(1+r*t)
    """

    funcion = capital * (1 + tasa * t)

    return diff(funcion, t)


def derivada_compuesta(capital, tasa, frecuencia=1):
    """
    Derivada del interés compuesto
    C(t)=C0(1+r/n)^(n*t)
    """

    funcion = capital * ((1 + tasa / frecuencia) ** (frecuencia * t))

    return diff(funcion, t)


def evaluar_derivada(derivada, tiempo):
    """
    Evalúa la derivada en un instante de tiempo.
    """

    return float(N(derivada.subs(t, tiempo)))