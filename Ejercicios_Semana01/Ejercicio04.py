"""
Contador de dígitos pares e impares:
Solicita un número entero largo, y con un bucle determina cuántos dígitos son pares y
cuántos impares.
"""

numero = input("Ingresa un número entero largo: ")
pares = 0
impares = 0

for i in numero:
  if int(i)%2==0:
    pares += 1
  else:
    impares += 1

print("Cantidad de dígitos pares:", pares)
print("Cantidad de dígitos impares:", impares)