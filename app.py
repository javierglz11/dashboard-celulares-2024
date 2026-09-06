import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página web
st.set_page_config(page_title="Dashboard Celulares 2024", layout="wide")

# ==========================================
# 1. ENCABEZADO PRINCIPAL DE LA APLICACIÓN
# ==========================================
st.header("Tablero de Análisis: Mercado de Celulares 2024")
st.write("Bienvenido al explorador interactivo del catálogo tecnológico global. Utiliza las herramientas de abajo para analizar los datos.")

# Carga optimizada de datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv('celulares_2024.csv')
    columnas_utiles = [
        'phone_brand', 'phone_model', 'display_type', 'usb', 
        'colors', 'video', 'chipset', 'cpu', 'gpu', 'os_type',
        'price_usd', 'storage', 'ram', 'battery'
    ]
    return df[columnas_utiles]

df_celulares = cargar_datos()

# ==========================================
# 2. ENCABEZADO PARA EL EXPLORADOR DE DATOS
# ==========================================
st.header("Explorador de Datos")
st.write("A continuación se muestra la tabla completa de los teléfonos registrados del año 2024. Puedes ordenarla haciendo clic en los títulos de las columnas.")

incluir_marcas_pequenas = st.checkbox("Incluir marcas con menos de 20 modelos en el mercado", value=True)

if not incluir_marcas_pequenas:
    conteo_marcas = df_celulares['phone_brand'].value_counts()
    marcas_grandes = conteo_marcas[conteo_marcas >= 20].index
    df_mostrar = df_celulares[df_celulares['phone_brand'].isin(marcas_grandes)]
else:
    df_mostrar = df_celulares

st.dataframe(df_mostrar, use_container_width=True)

# ==========================================
# 3. ENCABEZADO PARA EL ANÁLISIS GRÁFICO (con casillas)
# ==========================================
st.header("Análisis Visual de Tendencias")
st.write("Selecciona una o ambas casillas de verificación para desplegar los gráficos interactivos basados en los datos filtrados. (づᴗ _ᴗ)づ♡.")

# Creamos dos columnas para colocar las casillas de verificación de forma ordenada
col_chk1, col_chk2 = st.columns(2)

with col_chk1:
    mostrar_histograma = st.checkbox("Desplegar Histograma de Distribución de Precios.")

with col_chk2:
    mostrar_dispersion = st.checkbox("Desplegar Diagrama de Dispersión (RAM vs Precio).")

# --- LÓGICA DE RENDERIZADO DINÁMICO ---

# 1. Si el usuario seleccionó el Histograma
if mostrar_histograma:
    st.write("**Histograma Activo:** Analizando rangos de precio en el mercado... (｡•̀ᴗ-)✧")
    fig_hist = px.histogram(
        df_mostrar, 
        x='price_usd', 
        color='phone_brand',
        title='Distribución de Precios por Marca (2024)',
        labels={'price_usd': 'Precio (USD)', 'count': 'Modelos', 'phone_brand': 'Marca'},
        barmode='stack',
        nbins=30
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# 2. Si el usuario seleccionó la Dispersión
if mostrar_dispersion:
    st.write("**Diagrama de Dispersión Activo:** Analizando la tendencia de Costo según la RAM... (·'╻'·)")
    fig_scatter = px.scatter(
        df_mostrar, 
        x='ram', 
        y='price_usd', 
        color='phone_brand',
        hover_data=['phone_model'],
        title='Impacto de la Memoria RAM en el Precio (2024)',
        labels={'ram': 'RAM (GB)', 'price_usd': 'Precio (USD)', 'phone_brand': 'Marca'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# 3. Si no hay ninguna casilla seleccionada, dejamos un mensaje de guía
if not mostrar_histograma and not mostrar_dispersion:
    st.write("*Por favor, selecciona alguna casilla de verificación para visualizar un gráfico. ദ്ദി◝ ⩊ ◜.ᐟ*")

# =============================================================
# 4. ENCABEZADO: COMPARATIVA AVANZADA ENTRE DOS MARCAS
# =============================================================
st.header("Comparador de Distribución de Precios entre Marcas")
st.write("Selecciona dos marcas específicas de la lista para comparar directamente sus rangos de precios en el mercado.")

# 1. Obtenemos la lista única de marcas disponibles entre los datos y las ordenamos.
lista_marcas = sorted(df_celulares['phone_brand'].unique())

# 2. Creamos dos columnas para colocar los menús desplegables lado a lado
col_marca1, col_marca2 = st.columns(2)

with col_marca1:
    # Menú desplegable para la Marca 1
    marca_1 = st.selectbox("Selecciona la Marca 1", options=lista_marcas, index=0)

with col_marca2:
    # Menú desplegable para la Marca 2 (intentamos que por defecto elija otra de la lista)
    indice_defecto = 1 if len(lista_marcas) > 1 else 0
    marca_2 = st.selectbox("Selecciona la Marca 2", options=lista_marcas, index=indice_defecto)

# 3. Casilla para normalizar el histograma (pasar a porcentaje)
normalizar = st.checkbox("Normalizar histograma (Ver en porcentaje %)", value=True)

# 4. Filtramos los datos basándonos estrictamente en las dos marcas elegidas
df_comparativa = df_celulares[df_celulares['phone_brand'].isin([marca_1, marca_2])]

# 5. Definimos los parámetros dinámicos según la casilla de normalización
hist_norm_param = 'percent' if normalizar else None

# 6. Construimos el gráfico de plotly superpuesto)
fig_comp = px.histogram(
    df_comparativa, 
    x='price_usd', 
    color='phone_brand',
    barmode='overlay',          # Superpone las barras de forma limpia
    histnorm=hist_norm_param,   # Cambia dinámicamente entre conteo o porcentaje
    opacity=0.6,                # Transparencia para que se aprecien ambos colores
    title=f'Distribución de Precios: {marca_1} vs {marca_2}',
    labels={'price_usd': 'Precio (USD)', 'percent': 'Porcentaje (%)', 'phone_brand': 'Marca'},
    nbins=25
)

# 7. Desplegamos el gráfico interactivo en la pantalla web
st.plotly_chart(fig_comp, use_container_width=True)