# Diagrama de Clases

## Vehiculo
- Atributos:
  - marca: str
  - modelo: str
  - numero_ruedas: int
- Métodos:
  - to_dict(): dict

## Automovil (hereda de Vehiculo)
- Atributos:
  - velocidad: int
  - cilindrada: int
- Métodos:
  - to_dict(): dict

## Particular (hereda de Automovil)
- Atributos:
  - numero_puestos: int
- Métodos:
  - to_dict(): dict

## Carga (hereda de Automovil)
- Atributos:
  - peso_carga: int
- Métodos:
  - to_dict(): dict

## Bicicleta (hereda de Vehiculo)
- Atributos:
  - tipo: str
- Métodos:
  - to_dict(): dict

## Motocicleta (hereda de Bicicleta)
- Atributos:
  - motor: str
  - cuadro: str
  - nro_radios: int
- Métodos:
  - to_dict(): dict
