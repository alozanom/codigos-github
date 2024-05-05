import os
os.system ('cls')

def calcular_consumo_while(N):
    contador = 0
    while contador < N:
        identificacion = input("Ingrese la identificación: ")
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la dirección: ")
        num_medidor = input("Ingrese el número del medidor: ")
        lectura_anterior = float(input("Ingrese la lectura anterior: "))
        lectura_actual = float(input("Ingrese la lectura actual: "))

        consumo = lectura_actual - lectura_anterior

        print("\nIdentificación:", identificacion)
        print("Nombre:", nombre)
        print("Dirección:", direccion)
        print("Número del medidor:", num_medidor)
        print("Lectura actual:", lectura_actual)
        print("Lectura anterior:", lectura_anterior)
        print("Consumo del mes:", consumo)
        print("\n")

        contador += 1


N = int(input("Ingrese el número de usuarios a procesar: "))
calcular_consumo_while(N)
