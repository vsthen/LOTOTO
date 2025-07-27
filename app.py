import streamlit as st
import random
import datetime

st.set_page_config(page_title="LotoPool Daily", layout="centered")

# Título
st.title("🎟️ LotoPool Daily")
st.write("Tu generador diario de boletos de lotería")

# Fecha de inicio del reto
fecha_inicio = datetime.date(2025, 9, 1)
hoy = datetime.date.today()
dias_transcurridos = (hoy - fecha_inicio).days + 1

# 🔒 Generar los 320 boletos una sola vez y dividir en 32 días
@st.cache_data
def generar_boletos_totales():
    todos_los_boletos = set()
    lista_boletos = []

    # Paso 1: Generar 320 boletos únicos
    while len(lista_boletos) < 320:
        boleto = tuple(sorted(random.sample(range(1, 38), 6)))
        if boleto not in todos_los_boletos:
            lista_boletos.append(boleto)
            todos_los_boletos.add(boleto)

    # Paso 2: Asignar 10 boletos a cada uno de los 32 días
    boletos_por_dia = {}
    for dia in range(1, 33):
        inicio = (dia - 1) * 10
        fin = dia * 10
        boletos_por_dia[dia] = lista_boletos[inicio:fin]

    return boletos_por_dia

# Obtener los boletos para cada día
boletos_por_dia = generar_boletos_totales()

# Validar si el día actual es válido (1–32)
if dias_transcurridos < 1 or dias_transcurridos > 32:
    st.warning("Este no es un día válido del reto (1–32).")
else:
    st.subheader(f"Día {dias_transcurridos} de 32")
    if st.button("🎰 Generar 10 boletos de hoy"):
        st.success("¡Aquí están tus números de la suerte de hoy!")
        boletos = boletos_por_dia[dias_transcurridos]
        for i, boleto in enumerate(boletos, 1):
            st.write(f"Boleto {i}: {' - '.join(str(n) for n in boleto)}")

st.caption("Los boletos cambian cada día después de las 5:00 PM.")
