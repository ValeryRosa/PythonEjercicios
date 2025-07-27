"""
Número máximo entre cuatro números:
Declara cuatro variables a, b, c y d con valores numéricos. Utiliza condicionales
para determinar cuál de los cuatro números es el mayor y muéstralo.
"""

a = 25
b = 40
c = 32
d = 18

if a >= b and a >= c and a >= d:
    mayor = a
elif b >= a and b >= c and b >= d:
    mayor = b
elif c >= a and c >= b and c >= d:
    mayor = c
else:
    mayor = d

print("El número mayor es:", mayor)
