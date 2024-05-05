# Nombre & Materia del estudiante

Nombre = input("Andres estudiante de programación")
# Notas de cada corte del estudiante
nota_1 = float(input("Ingrese el primer corte: "))
nota_2 = float(input("Ingrese el segundo corte: "))
nota_3 = float(input("Ingrese el tercer corte: "))

# La nota definitiva
nota_defin = (nota_1 * 0.30) + (nota_2 * 0.30) + (nota_3 * 0.40)

# Mostrar la definitiva 
print(f"Su nota definitiva es: {nota_defin}")
