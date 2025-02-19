from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

st.title('Análise para predição dos valores de fechamento do índice Bovespa')

tab0, tab1 = st.tabs(['Análise Exploratória', 'Modelo'])

df = pd.read_csv('Dados Históricos - Ibovespa.csv')

df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
df = df[['Data', 'Último']]
df.columns = ['ds', 'y']
df = df.set_index('ds')

with tab0:
    plt.figure()
    sns.lineplot(data=df, x='ds', y='y')
    plt.xlabel('Ano')
    plt.ylabel('Valor (R$) (em milhares)')
    plt.title('Índice Bovespa')
    st.pyplot(plt)

    plt.figure()
    resultados = seasonal_decompose(df, period=247)
    fig, axes = plt.subplots(4, 1, figsize=(15,10))
    resultados.observed.plot(ax=axes[0])
    resultados.trend.plot(ax=axes[1])
    resultados.seasonal.plot(ax=axes[2])
    resultados.resid.plot(ax=axes[3])
    plt.tight_layout()
    st.pyplot(plt)