import plotly.graph_objects as go


def grafico_dashboard(datos):

    x = []
    y = []

    for fila in datos:

        x.append(fila[0])
        y.append(fila[1])

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=x,
            y=y,

            mode="lines+markers",

            name="Capital Final"

        )

    )

    fig.update_layout(

        title="Evolución de las Simulaciones",

        xaxis_title="Simulación",

        yaxis_title="Capital Final ($)",

        template="plotly_white",

        height=500,

        autosize=True

    )

    return fig.to_html(full_html=False, config={"responsive": True})