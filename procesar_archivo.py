import os
import csv
import tempfile
from werkzeug.utils import secure_filename
from datetime import datetime
from datetime import date

from modelos import Cuenta, CuentaJoven
from persona import Persona
from utils import obtener_edad, str_to_date

UPLOAD_FOLDER = tempfile.gettempdir()


def guardar_archivo(archivo)-> str:
    nombre_archivo = secure_filename(archivo.filename)
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    archivo.save(ruta_archivo)
    return ruta_archivo



def procesar_archivo(archivo: str):
    cuentas = []
    with open(archivo, mode="r") as file:
        archivo_csv = csv.reader(file)
        next(archivo_csv)
        nro_de_cuenta = 1
        for nombre, dni, fecha_nacimiento in archivo_csv:
            persona = Persona(nombre, dni, fecha_nacimiento)
            if not persona.es_mayor_de_edad():
                print("Hubo un Error: la persona es menor de edad")
            else:
                if 18 <= persona.edad< 30:
                    cuenta = CuentaJoven(persona, nro_de_cuenta, 50, saldo=0)
                    nro_de_cuenta += 1
                    cuentas.append(cuenta)
                else:
                    cuenta = Cuenta(persona, nro_de_cuenta, saldo=0, activa=True)
                    nro_de_cuenta += 1
                    cuentas.append(cuenta)
    return cuentas


def transformar_cuentas_a_dict(cuentas):
    cuentas_as_dict= []
    for cuenta in cuentas:
        cuentas_as_dict.append(cuenta.to_dict())
    return cuentas_as_dict

def guardar_cuentas(cuentas):
    cuentas = transformar_cuentas_a_dict(cuentas)
    with open ("cuentas.csv", "w") as csvfile:
        fieldnames = ["titular", "numero_de_cuenta", "saldo", "activa"]
        cuentas_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        cuentas_csv.writeheader()
        cuentas_csv.writerows(cuentas)
        






   








