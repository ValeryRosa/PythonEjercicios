#DICCIONARIOS: mutables solo en valores, se usan {}
estudiante={
  "nombre":["Valery","Luis","Roberta"],
  "edad": 21,
  "carrera":"Sistemas"
}
print(estudiante["nombre"])
estudiante["edad"]=23
estudiante["semestre"]=5
valor=estudiante["nombre"][1]
valor=estudiante.get("direccion", "no especificado")
items=estudiante.items()
print(estudiante["edad"])
print(estudiante["semestre"])
claves=estudiante.keys()
edad=estudiante.pop("edad")
valores=estudiante.values()
estudiante.clear() #Elimina todo el contenido del diccionario
print(edad)
print(items)
print(valores)
print(claves)




universidad={
  "estudiante":{
    "001":{"nombre":"Ana", "edad":20},
    "002":{"nombre":"Juan", "edad":21}
  },
  "cursos":["Matematica", "Fisica"]
}