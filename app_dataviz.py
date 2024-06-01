#Nome:Janaina Vicente dos Santos RA:2302926 

import sqlalchemy as sqa
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#Dados em um DataFrame
df = pd.read_csv('../0_bases_originais/dados_originais.csv', delimiter=";")

# App Bilheteria 
st.header('APP BILHETERIA', divider='red')

# Lateral
st.sidebar.header('Selecione o Filme')

filme_selecionado = st.sidebar.selectbox('Filme', df['filme'])

# Informçao central 
filme_data = df[df['filme'] == filme_selecionado]

st.write('Dados do Filme Selecionado')
st.write(filme_data)

st.write('Relação Geral')
st.dataframe(df, width=1000, height=500, hide_index=True)  # Mesmo que st.write(df)


def top_10_filmes(dados_filmes):
    # Ordena os dados dos filmes pela bilheteria convertida em inteiro em ordem decrescente
    filmes_ordenados = sorted(dados_filmes, key=lambda x: int(x.split(';')[0].replace(' ', '')), reverse=True)

    # Seleciona os 10 primeiros filmes
    top_10 = filmes_ordenados[:10]

    # Imprime os 10 primeiros filmes
    for filme in top_10:
        print(filme)

# Dados dos filmes fornecidos
dados_filmes = [
    "2 923 706 026;1;2009;Avatar;20th Century Fox;James Cameron",
    "2 799 439 100;2;2019;Vingadores: Ultimato;Walt Disney Studios Motion Pictures;Joe Russo / Anthony Russo",
    # Adicione os outros dados dos filmes aqui...
]

# Chama a função para mostrar os 10 melhores filmes
top_10_filmes(dados_filmes)

