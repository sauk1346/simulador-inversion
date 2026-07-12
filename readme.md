# Simulador de ahorro e inversión

Simulador web (Flask) que muestra la evolución de un capital ahorrado o
invertido en el tiempo, junto con su derivada (velocidad de crecimiento) y su
límite cuando el tiempo tiende a infinito.

Proyecto de la asignatura [CVCD01] Cálculo Diferencial — Ingeniería
Informática, INACAP.

## Requisitos

- Python 3.12
- `pip` y el módulo `venv` (en Ubuntu/Debian: `sudo apt install python3-pip python3.12-venv`)

## Instalación

```bash
cd proyecto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
source venv/bin/activate
python app.py
```

Abre http://127.0.0.1:5000 en el navegador. Para detener el servidor: `Ctrl+C`.

## Estructura

- `app.py` — rutas Flask.
- `calculos/` — modelo matemático (interés simple/compuesto, derivadas,
  límites, inflación, riesgo, recomendaciones, escenarios).
- `database.py` — historial de simulaciones en SQLite (`simulador.db`).
- `utils/pdf.py` — exportación de una simulación a PDF (usa `reportlab`).
- `templates/`, `static/` — interfaz web (Bootstrap 5 + Plotly + MathJax).