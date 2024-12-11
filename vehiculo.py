class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "marca": self.marca,
            "modelo": self.modelo,
            "numero_ruedas": self.numero_ruedas
        }