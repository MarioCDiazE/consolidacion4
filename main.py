import csv
from particular import Particular
from carga import Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from vehiculo import Vehiculo
from automovil import Automovil

def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([vehiculo.__class__, vehiculo.to_dict()])
    except Exception as e:
        print(f"Error al guardar los datos en el archivo {nombre_archivo}: {e}")

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for row in archivo_csv:
                print(f"Lista de Vehiculos {row[0]} {row[1]}")
    except Exception as e:
        print(f"Error al leer los datos del archivo {nombre_archivo}: {e}")

def main():
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    guardar_datos_csv(vehiculos)
    leer_datos_csv()

    print("\nVerificando relaciones de instancia de motocicleta:")
    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

if __name__ == "__main__":
    main()