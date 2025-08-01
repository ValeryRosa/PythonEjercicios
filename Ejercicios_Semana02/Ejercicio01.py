class Perro:
  especie="Chihuahua"

  def __init__(self, nombre, edad):
    self.nombre=nombre
    self.edad=edad

  def ladrar(self):
    return f"{self.nombre} esta ladrando"

  def describir(self):
    return f"{self.nombre} tiene {self.edad} años"

perro1= Perro("Charlie", 3)
perro2= Perro("Luna", 5)
print(perro1.ladrar())
print(perro2.ladrar())
print(perro1.describir())
print(Perro.especie)