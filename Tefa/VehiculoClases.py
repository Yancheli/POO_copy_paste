# clase padre o principal
class Vehiculo:
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año

   
    def detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, año {self.año}")

   
    def encender(self):
        print(f"El {self.marca} vehículo se prendió")

    
    def frenar(self):
        print(f"El {self.marca} vehículo se detuvo")

    def sonido(self):
        print (f"El vehículo {self.marca} esta sonando la bocina")


# Clase hija 1
class Electrico(Vehiculo):
    def __init__(self, marca, modelo, color, año, puertas):
        super().__init__(marca, modelo, color, año)
        self.puertas = puertas

    def encender(self):
        print("El carro enciende con un sonidito musical")

    # Método propio
    def abrir_puerta(self):
        print("Ya te puedes subir")


# Clase hija 2
class Tradicional(Vehiculo):
    def __init__(self, marca, modelo, color, año, tipo):
        super().__init__(marca, modelo, color, año)
        self.tipo = tipo 

    def encender(self):
        print("El vehiculo ruge al encender")

    # Método propio
    def cargar_gasolina(self):
        print("Se ha llenado el tanque del vehiculo")

#creo los objetos
Bestune = Electrico("Bestune", "Xiaoma", "Rosa", 2023, 4)
Toyota = Tradicional("Toyota", "Supra", "Rojo", 2020, "Sedán")

# Ejemplos

print("**Heredado**")
Bestune.detalles()
Toyota.detalles()

# Métodos sobreescritos
Bestune.encender()
Toyota.encender()

# Métodos propios
print("**Métodos propios**")
Bestune.abrir_puerta()
Toyota.cargar_gasolina()

# Metodos del principal que igual sirven
Bestune.frenar()
Toyota.sonido()
