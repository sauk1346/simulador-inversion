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
cd version-antonio
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

## Diferencias respecto a `version-khris`

**Matemática y LaTeX**
- Las tarjetas de Derivada y Límite se renderizan como LaTeX real (vía
  `sympy.latex` + MathJax) en vez de texto plano de sympy, con el símbolo de
  multiplicación explícito y números redondeados para que sean legibles.
- La sección de notación matemática muestra la fórmula que corresponde al
  tipo de interés elegido (simple o compuesto), en vez de mostrar siempre
  la fórmula de interés compuesto.
- Nuevo: selector de **frecuencia de capitalización** (anual/semestral/
  trimestral/mensual) para el interés compuesto, con una tabla comparativa
  en los resultados. Esto responde la pregunta orientadora de Etapa I sobre
  frecuencia de capitalización, que no estaba implementada.

**Rediseño para que sea intuitivo sin conocimientos de cálculo**
- La página de resultados ya no muestra la derivada/límite en bruto como
  primer contacto: primero explica en español simple qué significa el
  resultado para la plata del usuario, y deja la notación matemática
  formal detrás de un botón "Ver la notación matemática (opcional)".
- `educacion.html` antepone una analogía cotidiana (la derivada como
  "velocímetro del dinero", el límite como "dejar crecer tu plata para
  siempre") antes de cada fórmula.
- `index.html` ya no muestra un dashboard en $0 en la primera visita: si no
  hay simulaciones guardadas, muestra una bienvenida con una sola llamada
  a la acción en vez de estadísticas vacías.
- `simulador.html` agrega una explicación en lenguaje simple bajo cada
  campo del formulario.

**Correcciones**
- El gráfico de "Crecimiento de la inversión" usaba un tema oscuro
  (`plotly_dark`) que desentonaba con el resto del sitio (claro); ahora usa
  el mismo tema que el resto de los gráficos.
- El título y la leyenda del gráfico de "Comparación Visual" se
  superponían; se separaron con más margen.
- Se agregó `reportlab` a `requirements.txt` (lo usa `utils/pdf.py` pero
  faltaba, así que la exportación a PDF fallaba en una instalación limpia).
- Se eliminó el enlace a `css/estilos.css` (archivo inexistente).
- El JS que vivía inline en `base.html` se movió a `static/js/script.js`.
