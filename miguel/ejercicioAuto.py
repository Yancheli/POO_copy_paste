class Vehiculos:
   def __init__ (self,Nombre,Marca,Color,hibrido,):
        self.Nombre = Nombre
        self.Marca = Marca
        self.Color = Color
        self.hibrido = hibrido
   def es_hibrido(self):
        if self.hibrido:
            print(f"El vehiculo {self.Nombre} es hibrido.")
        else:
            print(f"El vehiculo {self.Nombre} no es hibrido.")     
   def bateria(self):
        if self.hibrido:
            print(f"El vehiculo {self.Nombre} tiene bateria electrica.")
        else:
            print(f"El vehiculo {self.Nombre} no tiene bateria electrica.")
   def cargar(self):
        if self.hibrido:
            print(f"El vehiculo {self.Nombre} se puede cargar.")
        else:
            print(f"El vehiculo {self.Nombre} no necesita cargarse.")
class hibrido(Vehiculos):
    def __init__(self, Nombre, Marca, Color,hibrido ):
        super().__init__(Nombre, Marca, Color,hibrido= True)
        self.hibrido = hibrido


class No_Hibrido(Vehiculos):
    def __init__(self, Nombre, Marca, Color,hibrido ):
        super().__init__(Nombre, Marca, Color,hibrido= False)
        self.hibrido = hibrido

auto= hibrido ("Tesla", "Model S", "Rojo", True)

auto2= No_Hibrido ("Ford", "Mustang", "Azul", False)

auto.cargar()
auto2.cargar()

