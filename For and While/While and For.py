import os
os.system ('cls')

def es_primo_while(numero):
    if numero < 2:
        return False
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1
    return True

numero = int(input("Ingrese un número entero positivo: "))
if es_primo_while(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
