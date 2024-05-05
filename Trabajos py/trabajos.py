#Programa : punto1.py
temperaturas = [44, 22, 15, 75]
# Mostrar cada temperatura registrada y su valor
for i, temp in enumerate(temperaturas, 1):
    print(f"Temperatura {i}: {temp}")

# Calcular el promedio de las temperaturas
promedio = sum(temperaturas) / len(temperaturas)

# Mostrar el promedio de las temperaturas
print(f"Promedio de temperaturas: {promedio}")