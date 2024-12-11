from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "motor": self.motor,
            "cuadro": self.cuadro,
            "nro_radios": self.nro_radios
        })
        return data