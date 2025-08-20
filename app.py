import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Caminho correto para app.py, que está na raiz do projeto
csv_path = os.path.join("dados", "vehicles.csv")
car_data = pd.read_csv(csv_path)

st.title("Dashboard de Anúncios de Carros")

# Barra lateral
# Sidebar
st.sidebar.title("Filtros e Opções")
hist_button = st.sidebar.button("Criar Histograma")
dispersao_button = st.sidebar.checkbox("Criar Gráfico de Dispersão")

# Histograma
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    st.subheader("Histograma")
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão
if dispersao_button: # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write('Criando um Gráfico de Dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    st.subheader("Gráfico de Dispersão:")
    fig = px.scatter(car_data, x="odometer", y="price", color="year", hover_name="make", size="price", title="Gráfico de Dispersão: Odometer vs Price")
  
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)