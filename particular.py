from automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "numero_puestos": self.numero_puestos
        })
        return data