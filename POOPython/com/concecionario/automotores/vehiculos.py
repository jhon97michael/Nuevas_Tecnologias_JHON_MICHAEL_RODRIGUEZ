class Vehiculo:  # clase

    # Constructor
    def __int__(self, marca, modelo, color, ruedas, ref):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas
        self.ref = ref

    def ver_vehiculo(self):
        print(f"marca: {self.marca}\n Modelo: {self.modelo}")


moto = Vehiculo("Yamaha", 2023, "Negra", 2, "N-Max 150")

carro = Vehiculo("Mazda", 2024, "Blanco", 4, "CX-5")

carro.ver_vehiculo()



