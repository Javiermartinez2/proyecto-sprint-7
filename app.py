import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("data/vehicles_us.csv")  

st.header("Cuadro de mandos — Anuncios de vehículos")

st.subheader("Vista previa de los datos")
st.dataframe(car_data.head())

hist_button = st.button('Construir histograma') # crear un botón
if hist_button:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir dispersión (precio vs odómetro)')

if scatter_button:
    st.write('Gráfico de dispersión: precio vs odómetro')
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        opacity=0.6,
        title="Precio vs Odómetro"
    )
    st.plotly_chart(fig, use_container_width=True)
