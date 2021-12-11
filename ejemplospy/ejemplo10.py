class GrupoAnimal:
  x = 0
  nombre = ""
  def __init__(self, z):
    self.nombre = z
    print(self.nombre,"construido")  
    
  @classmethod
  def fromfilename(cls, filename):
    "Inicializa GrupoAnimal desde un fichero"
    nombre = open(filename).readlines()
    return cls(data)
    
  def __init__(self, y):
    self.x = y
    print("construido con un numero")

  def grupo(self) :
    self.x = self.x + 1
    print(self.nombre,"recuento grupal",self.x)

s = GrupoAnimal("Sally")
j = GrupoAnimal("Jim")

s.grupo()
j.grupo()
s.grupo()
