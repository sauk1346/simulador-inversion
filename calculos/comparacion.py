import plotly.graph_objects as go

from calculos.interes import (
    interes_simple,
    interes_compuesto,
    interes_compuesto_con_aportes
)


def grafico_comparacion(capital, tasa, tiempo, aporte):

    tiempos = []
    simple = []
    compuesto = []

    paso = 0.1
    t = 0

    while t <= tiempo:

        tiempos.append(round(t, 2))

        simple.append(
            interes_simple(
                capital,
                tasa,
                t
            )
        )

        if aporte > 0:

            compuesto.append(
                interes_compuesto_con_aportes(
                    capital,
                    tasa,
                    t,
                    aporte
                )
            )

        else:

            compuesto.append(
                interes_compuesto(
                    capital,
                    tasa,
                    t
                )
            )

        t += paso

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=tiempos,
            y=simple,

            mode="lines",

            name="Interés Simple"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=tiempos,
            y=compuesto,

            mode="lines",

            name="Interés Compuesto"
        )
    )





    compuesto_aportes = []

    t = 0

    while t <= tiempo:

        compuesto_aportes.append(

            interes_compuesto_con_aportes(
                capital,
                tasa,
                t,
                aporte
            )

        )

        t += paso

    fig.add_trace(

        go.Scatter(

            x=tiempos,

            y=compuesto_aportes,

            mode="lines",

            name="Compuesto + Aportes"

        )

    )




    fig.update_layout(
    title="Comparación de Modelos Matemáticos de Inversión",
    xaxis_title="Tiempo (años)",
    yaxis_title="Capital ($)",
    hovermode="x unified",
    template="plotly_white",
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.25,
        xanchor="center",
        x=0.5
    ),
    margin=dict(t=60, b=90),
    font=dict(
        size=16
    ),
    height=600,
    autosize=True
)
    return fig.to_html(full_html=False, config={"responsive": True})