import streamlit as st
import random

st.set_page_config(page_title="LotoPool Daily", page_icon="🎟️")

st.title("🎟️ LotoPool Daily")
dia = st.number_input("¿Qué día es hoy? (1–32)", min_value=1, max_value=32, step=1)

def generar_boleto():
    numeros = random.sample(range(1, 39), 5)
    numeros.sort()
    return numeros

if st.button("Generar 10 boletos"):
    st.subheader(f"🎟️ Boletos del día {dia}")
    for i in range(1, 11):
        boleto = generar_boleto()
        st.write(f"Boleto {i}: {boleto}")
