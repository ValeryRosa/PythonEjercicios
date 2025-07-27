"""
Suma condicional de múltiplos:
Pide un número N y suma solo los múltiplos de 3 o 5 hasta N. 
Muestra la suma y los múltiplos encontrados.
"""

def sumarMultiplos():
  n=int(input("Ingresa un numero n: "))
  suma=0
  multiplos=[]

  for i in range(1,n+1):
    if i%3==0 or i%5==0:
      multiplos.append(i)
      suma+=i

  print(f"Multiplos encontrados: :{multiplos}")
  print(f"Suma total: {suma}")

sumarMultiplos()