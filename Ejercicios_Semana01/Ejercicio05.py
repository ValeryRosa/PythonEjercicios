"""
Clasificación de productos:
Pide nombre, precio y categoría (tecnología, alimentos, ropa). Dependiendo de la
categoría y precio, aplica diferentes tipos de impuestos y clasificaciones (lujo, básico,
etc.).
"""

nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
categoria = input("Categoría (tecnología, alimentos, ropa): ").lower()

if categoria == "tecnología":
    impuesto = 0.18
elif categoria == "alimentos":
    impuesto = 0.05
elif categoria == "ropa":
    impuesto = 0.12
else:
    impuesto = 0
    print("Categoría no válida. No se aplicará impuesto.")

precio_final = precio + (precio * impuesto)

if precio >= 1000:
    clasificacion = "Producto de lujo"
elif precio >= 200:
    clasificacion = "Producto estándar"
else:
    clasificacion = "Producto básico"

print("\n--- Detalles del Producto ---")
print("Nombre:", nombre)
print("Categoría:", categoria)
print(f"Precio original: S/ {precio}")
print(f"Impuesto aplicado: {impuesto * 100}%")
print(f"Precio final con impuesto: S/ {precio_final}")
print("Clasificación:", clasificacion)
