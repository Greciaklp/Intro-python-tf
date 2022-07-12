from datetime import datetime, date
from typing import Type


def str_to_date(fecha: str) -> date:
    fecha = datetime.strptime(fecha, "%Y-%m-%d")
    fecha = fecha.date() 
    return fecha

def obtener_edad(fecha_1:date, fecha_2:date)-> int:
    edad = (fecha_1 - fecha_2).days / 365
    return  int(edad)


