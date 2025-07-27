"""
Evaluación de estudiantes:
Dado un array de estudiantes (nombre, notas[]), calcula el promedio individual y
muestra los que aprobaron (promedio ≥ 11) y su mención (suficiente, bueno, excelente).
"""

def evaluar_estudiantes():
  estudiantes=[
    {"Nombre":"Luis", "Notas":[11, 12, 13, 14]},
    {"Nombre":"Maria", "Notas":[16, 20, 15, 19]},
    {"Nombre":"Juana", "Notas":[15, 18, 14, 18]}
  ]
  print("Resultados de la evaluación: ")
  for estudiante in estudiantes:
    promedio=sum(estudiante["Notas"])/len(estudiante["Notas"])
    if promedio>=11:
      mensaje="suficiente"
      if promedio>=16:
        mensaje="excelente"
      elif promedio>=14:
        mensaje="bueno"
      print(f"{estudiante["Nombre"]:}: Promedio: {promedio}. Mención: {mensaje}")

evaluar_estudiantes()