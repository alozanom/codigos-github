# Función para calcular la cantidad de concreto requerida para un tramo
def calcular_concreto():
    nombre_ing = input("Ingrese el ingeniero a cargo: ")
    nombre_tramo = input("Ingrese el nombre del tramo: ")
    longitud_tramo = float(input("Ingrese la longitud del tramo en metros: "))
    espesor_concreto = float(input("Ingrese el espesor de concreto en metros: "))
    
    # Calcular volumen en metros cúbicos
    volumen = longitud_tramo * espesor_concreto
    
    # Mostrar resultado
    print(f"Ingeniero a cargo: {nombre_ing}")
    print(f"Nombre del tramo: {nombre_tramo}")
    print(f"Cantidad de concreto requerido en metros cúbicos para el tramo: {volumen} m³")
    print()

# Solicitar al usuario la cantidad de tramos a procesar
cantidad_tramos = int(input("Ingrese la cantidad de tramos a procesar: "))

# Procesar cada tramo
for _ in range(cantidad_tramos):
    calcular_concreto()
