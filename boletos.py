import random

# generar un solo boleto con 5 números únicos del 1 al 38
def generar_boleto():
    numeros = random.sample(range(1, 39), 5)
    numeros.sort()
    return numeros

# generar 10 boletos
def generar_boletos(dia_actual):
    print(f"🎟️ Boletos del día {dia_actual}:")
    for i in range(1, 11):
        boleto = generar_boleto()
        print(f"Boleto {i}: {boleto}")

# preguntar por el día
dia = input("¿Qué día es hoy (1–32)? ")
generar_boletos(dia)
