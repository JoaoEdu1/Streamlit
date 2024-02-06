import streamlit as st

st.set_page_config(page_title="Streamlit")

with st.container():
    if st.button("Contratos"):
        st.switch_page("pages/contratos.py")
    if st.button("Github locate"):
        st.switch_page("pages/git.py")
    if st.button("Coingecko"):
        st.switch_page("pages/pycoingecko.py")

def create_a_person():
    people_list = []


    with st.form(key="iclude_client"):
        with st.container():
            st.write("Hello new Client")
            inpt_name = st.text_input(label="Name")
            inpt_age = st.number_input(label="Age", format="%d", step=1)
            inpt_gender = st.selectbox(label="Selecione o seu gênero", options=["Masculino", "Feminino", "Outro"])
            inpt_btn_submit = st.form_submit_button("Enviar")

    if inpt_btn_submit:
        person = {"Name": inpt_name, "Age": inpt_age, "Gender": inpt_gender}
        people_list.append(person)

    st.write("Pessoa:")
    for person in people_list:
        st.write(person)

create_a_person()