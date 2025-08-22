class Animal:

  def __init__(self,Nombre, Edad, vivo =True):
    self.Nombre = Nombre
    self.Edad = Edad
    self.Vivo = vivo
  def comer(self):
    print(f"El animal {self.Nombre} está comiendo.")
  def sonido(self):
     if self.Vivo:
      print(f"El animal {self.Nombre} está haciendo un sonido.")
     else:
      print(f"El animal {self.Nombre} no puede hacer sonido porque no está vivo.")
class invertebrados(Animal):
    def __init__(self, Nombre, Edad, Tipo ):
        super().__init__(Nombre, Edad,vivo = True)
        self.Nombre = Nombre
        self.Edad = Edad    
        self.Vivo = True
        self.Tipo = Tipo
    def caminar(self):
     if self.Vivo:
        print(f"El animal {self.Nombre} se arrastra.")
     else :
        print(f"El animal {self.Nombre} no puede arrastrarse porque no está vivo.")
    
class vertebrados(Animal):
    def __init__(self, Nombre, Edad, Tipo):
        super().__init__(Nombre, Edad,vivo = True)
        self.Tipo = Tipo
        self.Nombre = Nombre
        self.Edad = Edad
        self.Vivo = True
    def caminar(self):
        if self.Vivo:
         print(f"El animal {self.Nombre} dio un paso.")
        else :
         print(f"El animal {self.Nombre} no puede caminar porque no está vivo.")
animalito = invertebrados("Gusano", 2,"salvaje")
animalote = vertebrados("Perro", 5,"domestico")
animalito.sonido()
animalote.sonido()
