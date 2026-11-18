from abc import ABC, abstractmethod

class MetodoPago(ABC):
    def __init__(self, monto):
        self.__monto = monto

    def obtener_monto(self):
        return self.__monto

    @abstractmethod
    def pagar(self):
        pass

class Efectivo(MetodoPago):
    def __init__(self, monto):
        super().__init__(monto)

    def pagar(self):
        print(f"Cobro de ${self.obtener_monto()} en efectivo realizado exitosamente")

class Credito(MetodoPago):
    def __init__(self, monto, cuotas, banco):
        super().__init__(monto)
        self.cuotas = cuotas
        self.banco = banco

    def pagar(self):
        valor_cuota = self.obtener_monto() / self.cuotas
        print(f"Cobro de ${self.obtener_monto()} en {self.cuotas} cuotas ${valor_cuota:.2f} con tarjeta crédito {self.banco} realizado exitosamente")

class Debito(MetodoPago):
    def __init__(self, monto, banco):
        super().__init__(monto)
        self.banco = banco

    def pagar(self):
        print(f"Cobro de ${self.obtener_monto()} con tarjeta de débito {self.banco} realizado exitosamente")

class NFC(MetodoPago):
    def __init__(self, monto, dipositivos):
        super().__init__(monto)
        self.dipositivos = dipositivos

    def pagar(self):
        print(f"Cobro de ${self.obtener_monto()} con Contacto NFC {self.dipositivos} realizado exitosamente")

class MercadoPago(MetodoPago):
    def __init__(self, monto, alias):
        super().__init__(monto)
        self.alias = alias

    def pagar(self):
        print(f"Cobro de ${self.obtener_monto()} con Mercado Pago {self.alias} realizado exitosamente")

if __name__ == "__main__":
    pago_efectivo = Efectivo(1000)
    pago_credito = Credito(500000, 12, "BBVA")
    pago_debito = Debito(4400000, "Galicia")
    pago_nfc = NFC(1600000, "Samsumg A34")
    pago_mp = MercadoPago(7700000, "samuel6789.mp")

    metodo_pagos = [pago_efectivo, pago_credito, pago_debito, pago_nfc, pago_mp]

    total_recaudado = 0
    for metodo in metodo_pagos:
        metodo.pagar()
        total_recaudado += metodo.obtener_monto()
    print(f"Se recaudo en total es {total_recaudado}")