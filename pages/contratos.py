import streamlit as st
import pandas as pd


st.set_page_config(page_title='DashBoard Contratual', layout="centered")

with st.container():
  st.title('Dashboard Contratual')
  st.header('Insira as Informações necessárias')

# Colocar dados dos services em cache
@st.cache_data
def run_dados():
  tab = pd.read_csv('./services/api.csv')
  return tab

# Ver ele em um grafico  e selecionar os dias que quer ver
with st.container():
  dados = run_dados()
  qntd_days = st.selectbox('selecione o período',['7D','15D', '30D', '50D' ])
  num_day = int(qntd_days.replace('D', ''))
  dados = run_dados()
  dados= dados[-num_day:]
  st.area_chart(dados,x='Data', y='Contratos')

