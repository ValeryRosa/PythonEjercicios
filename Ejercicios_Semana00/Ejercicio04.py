"""
Calculadora simple:
Declara tres variables: a (un número), operador (un operador aritmético como
cadena), y b (otro número). Utiliza condicionales para realizar la operación
correspondiente y muestra el resultado.
"""


a = 10
operador = "+"
b = 5

if operador == "+":
    resultado = a + b
elif operador == "-":
    resultado = a - b
elif operador == "*":
    resultado = a * b
elif operador == "/":
    if b != 0:
        resultado = a / b
    else:
        resultado = "Error: División por cero"
elif operador == "%":
    if b != 0:
        resultado = a % b
    else:
        resultado = "Error: Módulo por cero"
else:
    resultado = "Operador no válido"

print("Resultado:", resultado)
