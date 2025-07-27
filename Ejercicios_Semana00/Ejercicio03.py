"""
Determina el rango de un número:
Declara una variable número con un valor numérico y utiliza condicionales para
determinar en qué rango se encuentra.
"""

numero = 72


if numero < 0:
    print("El número es negativo.")
elif numero <= 10:
    print("El número está entre 0 y 10.")
elif numero <= 20:
    print("El número está entre 11 y 20.")
elif numero <= 30:
    print("El número está entre 21 y 30.")
elif numero <= 40:
    print("El número está entre 31 y 40.")
elif numero <= 50:
    print("El número está entre 41 y 50.")
elif numero <= 60:
    print("El número está entre 51 y 60.")
elif numero <= 70:
    print("El número está entre 61 y 70.")
elif numero <= 80:
    print("El número está entre 71 y 80.")
elif numero <= 90:
    print("El número está entre 81 y 90.")
elif numero <= 100:
    print("El número está entre 91 y 100.")
else:
    print("El número es mayor que 100.")

