from datetime import datetime, date
from typing_extensions import Self

from utils import obtener_edad, str_to_date, obtener_edad
from modelos import Cuenta


class Persona:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self._nombre = nombre
        self._dni = dni
        self._fecha_nacimiento = str_to_date (fecha_nacimiento)
        

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @property 
    def edad(self):
        return obtener_edad(date.today(), self._fecha_nacimiento)

    def mostar_persona(self):
        return f"Nombre:{self._nombre} - Dni: {self._dni} - Fecha_de_nacimiento: {self._fecha_nacimiento}"


    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
          

   

    

   

        
  



    

