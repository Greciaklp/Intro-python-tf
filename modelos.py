from datetime import datetime, date

class Cuenta: 
    def __init__(self, titular, nro_de_cuenta, saldo=0, activa=True ):
        self._titular = titular
        self._nro_de_cuenta= nro_de_cuenta
        self._saldo = saldo
        self._activa = activa
        
        
       
    @property
    def titular(self):
        return self._titular

    @property
    def nro_de_cuenta(self):
        return self._nro_de_cuenta
        
    @property
    def saldo(self):
        return self._saldo

    @property
    def activa(self):
        return self.activa

    @saldo.setter
    def saldo(self, saldo):
        raise Exception("el saldo no puede ser modificado")

    @nro_de_cuenta.setter
    def nro_de_cuenta(self, nro_de_cuenta):
        return Exception("el nro de cuenta no puede ser modificado")

    def mostrar(self):
        return f"titular:{self._titular} - Saldo: {self._saldo}"
    
    def aplicar_deposito(self, cantidad):
        if cantidad > 0:
            self._saldo = self.saldo + cantidad
            self.crear_movimiento("deposito", cantidad)
        
    def aplicar_gasto(self, cantidad):
        self._saldo = self._saldo - cantidad
        self.crear_movimiento("gasto", cantidad)

    def _crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)
    
    @property
    def movimientos(self):
        return self.movimientos

    def to_dict(self):
        return {
            "titular": self._titular.nombre,
            "numero_de_cuenta": self._nro_de_cuenta,
            "saldo": self._saldo,
            "activa": self._activa
        }


class CuentaJoven(Cuenta):
    def __init__(self, titular, nro_de_cuenta, bonificacion, saldo=0):
        super().__init__(titular, nro_de_cuenta, saldo)
        self.bonificacion= bonificacion
    
    def es_titular_valido(self):
        return 18 <= self.titular.edad < 25
    
    def aplicar_gasto(self, cantidad):
        if self.es_titular_valido():
            super().aplicar_gasto(cantidad)
        else:
            raise Exception("No puede retirar dinero, no es un titular valido")

    def mostrar_cuentajoven(self):
        return f"""Se ha creado una Cuenta joven: numero de cuenta:{self._nro_de_cuenta} - 
        Titular: {self._titular} - saldo: {self._saldo} y tiene una bonificación del {self.bonificacion} % por un año"""



class MovimientoCuenta:
    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        return f"{self.fecha_y_hora} - {self.descripcion} - {self.monto}"

