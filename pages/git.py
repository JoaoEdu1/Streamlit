import requests as rq
import streamlit as st

BASE_URL = 'https://api.github.com'


def select_user(username):
  url = f'{BASE_URL}/users/{username}'
  response = rq.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None
  
def ui():
  st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html= True)
  st.title('Consulta GitHub')
  username = st.text_input(label='Insira o nome do usuário no git')

  if st.button('Buscar'):
    info_user = select_user(username)
    if info_user is not None:
      st.container()
      st.markdown(f'''
      <div class="card" style="width: 18rem;">
        <img src="{info_user['avatar_url']}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{info_user['login']}</h5>
          <p class="card-text">{info_user['bio']}</p>
          <a href="{info_user['html_url']}" class="btn btn-primary">Ver perfil</a>
        </div>
      </div>
      ''', unsafe_allow_html=True)
    else:
      st.write(f'Usuario {username} não encontrado!!')

ui()