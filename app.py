import streamlit as st
import random
import datetime

st.set_page_config(page_title="LotoPool Daily", layout="centered")

# Título
st.title("🎟️ LotoPool Daily")
st.write("Tu generador diario de boletos de lotería")

# Calcular el día automáticamente
fecha_inicio = datetime.date(2024, 7, 1)
hoy = datetime.date.today()
dias_transcurridos = (hoy - fecha_inicio).days + 1

# Validar que esté dentro de los 32 días
if dias_transcurridos < 1 or dias_transcurridos > 32:
    st.warning("Este no es un día válido del reto (1-32).")
else:
    st.subheader(f"Día {dias_transcurridos} de 32")

    if st.button("🎰 Generar 10 boletos de hoy"):
        st.success("¡Aquí están tus números de la suerte de hoy!")
        for i in range(1, 11):
            numeros = sorted(random.sample(range(1, 38), 6))
            st.write(f"Boleto {i}: {', '.join(str(n) for n in numeros)}")

st.caption("Los boletos cambian cada día después de las 5:00 PM.")
