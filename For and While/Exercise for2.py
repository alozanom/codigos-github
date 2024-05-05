import os
os.system ('cls')

def es_primo_for(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero positivo: "))
if es_primo_for(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
