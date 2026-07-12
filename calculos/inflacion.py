def capital_real(capital_final, inflacion, tiempo):
    inflacion = inflacion / 100
    return capital_final / ((1 + inflacion) ** tiempo)