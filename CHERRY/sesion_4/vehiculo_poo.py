#Crear una clase vehículo con 2 hijas, donde mínimo 4 atributos y 3 métodos (1 heredado del padre sin modificar)

# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_maxima = velocidad_maxima

    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} está encendido.")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")

    def mostrar_info(self):  # Este lo heredarán sin modificar
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, "
              f"Color: {self.color}, Vel. Máxima: {self.velocidad_maxima} km/h")


# Clase hija Carro
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, puertas):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.puertas = puertas

    def encender(self):
        print(f"El carro {self.marca} {self.modelo} está encendido con llave.")

    def abrir_maletero(self):
        print("El maletero del carro se ha abierto.")


# Clase hija Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, tipo):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.tipo = tipo  # Ejemplo: 'Deportiva', 'Scooter'

    def encender(self):
        print(f"La moto {self.marca} {self.modelo} está encendida con botón.")

    def hacer_caballito(self):
        print(f"La moto {self.marca} {self.modelo} está haciendo un caballito.")


# --- Uso ---
mi_carro = Carro("BMW", "240i", "Negro", 250, 2)
mi_moto = Moto("Ducati", "Panigale V4", "Rojo", 299, "Deportiva")

mi_carro.encender()
mi_carro.mostrar_info()  # Método heredado sin modificar
mi_carro.abrir_maletero()

print()

mi_moto.encender()
mi_moto.mostrar_info()  # Método heredado sin modificar
mi_moto.hacer_caballito()
