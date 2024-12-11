from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "velocidad": self.velocidad,
            "cilindrada": self.cilindrada
        })
        return data