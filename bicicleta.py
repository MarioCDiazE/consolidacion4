from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tipo_bicicleta": self.tipo
        })
        return data