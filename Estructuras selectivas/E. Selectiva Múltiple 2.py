precio = float(input("Ingrese el precio del producto: "))
if precio <= 10:
    print("Producto de categoría económica.")
elif precio <= 50:
    print("Producto de categoría media.")
else:
    print("Producto de categoría alta.")
