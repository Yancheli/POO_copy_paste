class vehiculo:
    def __init__(self, marca, diseño, color, velocidad_maxima):
        self.marca = marca
        self.diseño = diseño
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        
    def encendido(self):
        print(f"{self.marca} {self.diseño} está encendido.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Diseño: {self.diseño}, Color: {self.color}, Velocidad Máxima: {self.velocidad_maxima} km/h")

class automovil(vehiculo):
    def __init__(self, marca, diseño, color, velocidad_maxima, numero_llantas):
        super().__init__(marca, diseño, color, velocidad_maxima)
        self.numero_llantas = numero_llantas

    def acelerar_carro(self):
        print("El automóvil acelera.")

    def mostrar_info_auto(self):
        self.mostrar_info()
        print(f"Numero de llantas: {self.numero_llantas}")

class moto(vehiculo):
    def __init__(self, marca, diseño, color, velocidad_maxima, tipo_moto):
        super().__init__(marca, diseño, color, velocidad_maxima)
        self.tipo_moto = tipo_moto

    def hacer_caballito(self):
        print("La moto se está picando")

    def mostrar_informacion_moto(self):
        self.mostrar_info()
        print(f"Tipo de moto: {self.tipo_moto}")

el_auto = automovil("BMW", "I8", "Blanco con negro", 250, 4)
el_auto.encendido()
el_auto.acelerar_carro()
el_auto.mostrar_info_auto()

la_moto = moto("Yamaha", "R8", "Rojo", 300, "Deportivo")
la_moto.encendido()
la_moto.hacer_caballito()
la_moto.mostrar_informacion_moto()