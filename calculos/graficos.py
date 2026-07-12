import plotly.graph_objects as go

from calculos.interes import (
    interes_simple,
    interes_compuesto,
    interes_compuesto_con_aportes
)


def grafico_crecimiento(capital, tasa, tiempo, tipo, frecuencia=1, aporte=0):

    tiempos = []
    capitales = []

    paso = 0.1
    t = 0

    while t <= tiempo:

        tiempos.append(round(t, 2))

        if tipo == "simple":
            capitales.append(
                interes_simple(capital, tasa, t)
            )

        elif aporte > 0:
            capitales.append(
                interes_compuesto_con_aportes(capital, tasa, t, aporte)
            )

        else:
            capitales.append(
                interes_compuesto(capital, tasa, t, frecuencia)
            )

        t += paso

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=tiempos,
            y=capitales,

            mode="lines",

            name="Capital",

            line=dict(width=4)

        )

    )

    fig.update_layout(

        title="Crecimiento del Capital",

        xaxis_title="Tiempo (años)",

        yaxis_title="Capital ($)",

        template="plotly_white",

        autosize=True

    )

    return fig.to_html(full_html=False, include_plotlyjs="cdn", config={"responsive": True})