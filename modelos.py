from datetime import datetime, date


class Cuenta: 
    def __init__(self, titular, nro_de_cuenta, saldo=0 ):
        self._titular = titular
        self._nro_de_cuenta= nro_de_cuenta
        self._saldo = saldo
       
    @property
    def titular(self):
        return self._titular

    @property
    def nro_de_cuenta(self):
        return self.nro_de_cuenta
        
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        raise Exception("el saldo no puede ser modificado")

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

    def __str__(self) -> str:
        return (f'{self.titular}: {self.nro_de_cuenta}: {self.saldo}')
    

class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"
