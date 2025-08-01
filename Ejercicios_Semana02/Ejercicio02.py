class Animal:
  def __init__(self, nombre):
    self.nombre=nombre

  def hacer_ruido(self):
    return "Sonido del animal generico"

class Gato(Animal):
  def __init__(self, nombre, vidas=7):
    super().__init__(nombre)
    self.vidas=vidas

  def describir(self):
    return f"{self.nombre} tiene {self.vidas} años"
  
  def usar_vida(self):
    if self.vidas>0:
      self.vidas-=1
      return f"{self.nombre} perdió una vida. Le quedan {self.vidas} vidas"
    return f"{self.nombre} se quedo sin vidas"

animal1=Animal("Generico")
print(animal1.hacer_ruido())
gato1=Gato("Cosmico", 12)
print(gato1.describir())
print(gato1.usar_vida())