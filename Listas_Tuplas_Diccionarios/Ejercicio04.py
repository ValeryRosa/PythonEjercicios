#TUPLAS: No son mutables, se usan ()
coordenada= (10,20)
numeros=[1,2,3,4,5]
colores=("rojo", "verde", "azul","rojo")
un_elemento=(10,) #Colocar el valor y una coma
print(colores[1])
indice=colores.index("verde") #Método index
conteo=colores.count("rojo") #Cuenta las veces que se repite el elemento
lista_colores=list(colores) #Convertir de tupla a lista
tupla_numeros=tuple(numeros) #Convertir de lista a tupla
print(indice)
print(conteo)
print(lista_colores)