 # Tablero de Análisis: Mercado de Celulares 2024

Este proyecto es una **aplicación web interactiva** desarrollada en Python que permite explorar, analizar y visualizar de forma dinámica el catálogo de teléfonos celulares del año 2024. 

El objetivo principal es transformar datos brutos en información de valor para entender las tendencias de precios, componentes y marcas en el mercado tecnológico actual.

---

## ¿Para qué sirve esta aplicación web?

La aplicación sirve como una herramienta de toma de decisiones y análisis de mercado. Permite a los usuarios:
* **Explorar el catálogo completo** de dispositivos de manera cómoda e interactiva.
* **Analizar el impacto económico** que tienen ciertos componentes de hardware (como la memoria RAM) en el costo final del producto.
* **Comparar la estrategia de precios** de las marcas competidoras para identificar opciones de gama baja, media o alta.

---

## Funcionalidades Principales

Esta plataforma cuenta con tres módulos interactivos clave:

1. **Explorador de Datos Dinámico (Data Viewer):** 
   Una tabla interactiva donde el usuario puede examinar todos los registros del dataset (`celulares_2024.csv`). Incluye una casilla de verificación (*checkbox*) para ocultar o mostrar marcas minoritarias (con menos de 20 modelos) y limpiar la vista.
   
2. **Análisis Visual de Tendencias:**
   * **Histograma de Precios:** Muestra en qué rangos de costo se concentra la mayoría de los teléfonos del mercado, segmentado por bloques de colores según la marca.
   * **Diagrama de Dispersión (RAM vs Precio):** Permite evaluar si los teléfonos con más memoria RAM son necesariamente los más caros, ayudando a detectar dispositivos con buena relación calidad-precio.
   * *Ambos gráficos se controlan mediante casillas independientes para que el usuario decida qué visualizar.*

3. **Comparador de Marcas:**
   Dos menús desplegables (*selectbox*) que permiten seleccionar dos marcas frente a frente (por ejemplo, *Samsung vs Apple*). El sistema genera un histograma superpuesto y normalizado en porcentaje para evaluar de forma directa cuál tiene una tendencia de precios más elevada.

---

 ## Tecnologías utilizadas

* **Python 3.10** (estabilidad y compatibilidad de librerías)
* **Streamlit** (Desarrollo a la interfaz web)
* **Pandas** (para el análisis y manipulación de datos)
* **Plotly** (Visualización de gráficos interactivos) 
* **Render** (Publicación y despliegue en la nube)

---

## Instalación y Ejecución Local

**Clonar el repositorio:**
```bash
   git clone https://github.com/javierglz11/dashboard-celulares-2024.git 
   cd dashboard-celulares-2024
   ```

**Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

**Ejecutar la aplicación:**
   ```bash
   streamlit run app.py
   ```   

**URL de la aplicación en Render**
[Ir a la aplicación desplegada](https://dashboard-phones-2024.onrender.com)

---