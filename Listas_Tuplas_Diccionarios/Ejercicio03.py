#LISTAS: Son mutables, se usan[]
frutas=["manzana", "banana", "naranja"]
numeros=[1,2,3,4,5]
mezclas=[1,"hola",4.324]

frutas[1]="pera" #Reemplazar un elemento
frutas.append("uva") #Agregar un elemento a la lista
frutas.insert(1,"kiwi") #Agregar un elemento a la lista en una posición específica
frutas.remove("naranja") #Eliminar un elemento
ultimo=frutas.pop() #Eliminar el último elemento
longitud=len(numeros)
ordenada=sorted(frutas)
sub_lista=numeros[1:4]
primeros=numeros[:3] #Mostrar los primeross
ultimos=numeros[-2:] #Mostrar los ultimos, de atras hacia adelante
print(ultimos)
print(primeros)
print(ordenada)
print(longitud)
print(frutas[0])
print(mezclas[2])
print(sub_lista)
print(frutas)