import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Leer el archivo CSV en un DataFrame
# Cambia "tus_datos.csv" por el nombre de tu dataset
df = pd.read_csv("vehicles_us.csv")

# 2. Encabezado de la aplicación
st.header("Cuadro de Mandos de la Aplicación Web")

# 3. Mostrar casillas de verificación
mostrar_histograma = st.checkbox("Mostrar histograma")
mostrar_dispersion = st.checkbox("Mostrar diagrama de dispersión")

# 4. Histograma (se ejecuta SOLO si la casilla está marcada)
if mostrar_histograma:
    columna_hist = st.selectbox("Selecciona la columna para el histograma:", df.columns)
    fig_hist = px.histogram(df, x=columna_hist)
    st.write(f"Histograma de la columna **{columna_hist}**:")
    st.plotly_chart(fig_hist)

# 5. Diagrama de dispersión (se ejecuta SOLO si la casilla está marcada)
if mostrar_dispersion:
    x_axis = st.selectbox("Selecciona la variable para el eje X:", df.columns, index=0)
    y_axis = st.selectbox("Selecciona la variable para el eje Y:", df.columns, index=1)
    fig_scatter = px.scatter(df, x=x_axis, y=y_axis)
    st.write(f"Diagrama de dispersión entre **{x_axis}** y **{y_axis}**:")
    st.plotly_chart(fig_scatter)

# 6. Mensaje por defecto si no hay nada seleccionado
if not mostrar_histograma and not mostrar_dispersion:
    st.info("☝️ Marca una casilla arriba para comenzar a visualizar tus datos.")
    
    