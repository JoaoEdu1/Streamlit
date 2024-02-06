from pycoingecko import CoinGeckoAPI
import streamlit as st

# Criar uma instância do CoinGeckoAPI
cg = CoinGeckoAPI()

# Obter o nome da moeda inserida pelo usuário
crypto_id = st.text_input(label='Insira o nome de uma moeda')

# Verificar se o usuário inseriu algum texto antes de prosseguir
if crypto_id:
    # Obter os dados do preço da moeda em BRL
    crypto_data = cg.get_price(ids=crypto_id, vs_currencies='brl')
    
    # Verificar se a moeda existe na resposta da API
    if crypto_id in crypto_data:
        price_brl = crypto_data[crypto_id]['brl']
        st.write(f'Preço do {crypto_id.capitalize()}: R${price_brl}')
    else:
        st.write('Moeda não encontrada. Por favor, insira um nome de moeda válido.')
else:
    st.write('Por favor, insira o nome de uma moeda para visualizar seu preço em BRL.')
