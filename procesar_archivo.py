import os
import csv
import tempfile
from werkzeug.utils import secure_filename
from datetime import datetime
from datetime import date

from modelos import Cuenta
from persona import Persona
from utils import obtener_edad, str_to_date

UPLOAD_FOLDER = tempfile.gettempdir()


def guardar_archivo(archivo)-> str:
    nombre_archivo = secure_filename(archivo.filename)
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    archivo.save(ruta_archivo)
    return ruta_archivo


cuentas = []
def procesar_archivo(archivo: str):
    with open(archivo, mode="r") as file:
        archivo_csv = csv.reader(file)
        next(archivo_csv)
        for nombre, dni, fecha_nacimiento in archivo_csv:
            persona = Persona(nombre, dni, fecha_nacimiento)
            if persona.es_mayor_de_edad() == False:
                print("Hubo un Error: la persona es menor de edad")
            else:
                nro_cuenta = 1000123
                for nombre, dni, fecha_nacimiento in archivo_csv:
                    cuenta = Cuenta(persona, nro_cuenta, saldo=0)
                    cuenta = {
                        "titular": persona,
                        "numero_de_cuenta": Cuenta.nro_de_cuenta,
                        "saldo" : Cuenta.saldo,
                    }
                    nro_cuenta += 1
                    
                    cuentas.append(cuenta)
    return cuentas


def guardar_cuentas():
    with open ("cuentas.csv", "w") as csvfile:
        fieldnames = ["titular", "numero_de_cuenta", "saldo"]
        cuentas_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        cuentas_csv.writeheader()
        cuentas_csv.writerows(cuentas)
        






   








