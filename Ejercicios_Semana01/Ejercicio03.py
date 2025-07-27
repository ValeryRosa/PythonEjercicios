"""
Tablas cruzadas:
Genera la tabla de multiplicar del 1 al 12 para los números del 1 al 10. 
Imprime cada tabla en bloques separados.
"""

def tabla_cruzada():
  for i in range(1,11):
    print(f"La tabla de multiplicar del {i} es: ")
    for j in range(1,12):
      print(f"{i} x {j} = {i*j}")

tabla_cruzada()