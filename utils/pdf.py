from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def limpio(valor):
    """
    Muestra un número sin decimales innecesarios: 10.0 -> "10", 2.5 -> "2.5".
    """
    valor = float(valor)
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:g}"


def crear_pdf(simulacion, archivo):

    estilos = getSampleStyleSheet()

    pdf = SimpleDocTemplate(archivo)

    elementos = []

    elementos.append(
        Paragraph(
            "Reporte de Simulación",
            estilos["Title"]
        )
    )

    elementos.append(Spacer(1,20))

    elementos.append(
        Paragraph(
            f"<b>ID:</b> {simulacion[0]}",
            estilos["BodyText"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Capital:</b> ${simulacion[1]:,.0f}",
            estilos["BodyText"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Tasa:</b> {limpio(simulacion[2]*100)} %",
            estilos["BodyText"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Tiempo:</b> {limpio(simulacion[3])} años",
            estilos["BodyText"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Tipo:</b> {simulacion[4]}",
            estilos["BodyText"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Capital Final:</b> ${simulacion[5]:,.0f}",
            estilos["BodyText"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Ganancia:</b> ${simulacion[6]:,.0f}",
            estilos["BodyText"]
        )
    )

    pdf.build(elementos)