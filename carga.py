from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "peso_carga": self.peso_carga
        })
        return data