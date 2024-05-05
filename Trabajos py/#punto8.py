# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la parte entera de la división
parte_entera = numero1 // numero2

# Calcular el residuo
residuo = numero1 % numero2

# Mostrar los números ingresados, la parte entera y el residuo
print(f"Primer número: {numero1}")
print(f"Segundo número: {numero2}")
print(f"Parte entera de la división: {parte_entera}")
print(f"Residuo de la división: {residuo}")
