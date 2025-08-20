import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Caminho correto para app.py, que está na raiz do projeto
csv_path = os.path.join("dados", "vehicles.csv")

# Carrega o CSV
car_data = pd.read_csv(csv_path)

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write('Criando um histograma para a coluna odometer')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Configuração do Streamlit
#st.set_page_config(page_title="Histograma Interativo", layout="wide")
#st.title("Histograma Interativo de Vendas de Carros")
#st.sidebar.header("Configurações do Histograma")
#st.sidebar.write("Use os botões e caixas de seleção para criar histogramas interativos com os dados de vendas de carros.")
# Exibir os dados
#st.sidebar.subheader("Dados de Vendas de Carros")
#st.sidebar.dataframe(car_data.head(10), width=300, height=200)
# Exibir informações sobre o projeto
#st.sidebar.subheader("Sobre o Projeto")
#st.sidebar.write("Este projeto tem o intuito de criar histogramas interativos com os dados de vendas de carros. Você pode explorar os dados e visualizar a distribuição dos odômetros dos veículos.")
