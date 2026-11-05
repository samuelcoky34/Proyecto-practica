class MetodoPago:
    def __init__(self, monto):
        self.monto = monto

    def procesar(self):
        print(f"Procesando pago genérico de ${self.monto}...")

class MercadoPago(MetodoPago):
    def __init__(self, monto, alias):
        super().__init__(monto)
        self.alias = alias

    def pagar(self):
        print(f"Procesando el pago del alias {self.alias}. Cobro de ${self.monto} realizado exitosamente.")

class NFC(MetodoPago):
    def __init__(self, monto, dispositivo_nfc):
        super().__init__(monto)
        self.dispositivo_nfc = dispositivo_nfc

    def pagar(self):
        print(f"Procesando con el dispositivo {self.dispositivo_nfc}. Cobro de ${self.monto} realizado exitosamente.")

class Debito(MetodoPago):
    def __init__(self, monto, banco):
        super().__init__(monto)
        self.banco = banco

    def pagar(self):
        print(f"Procesando con la tarjeta de débito {self.banco}. Cobro de ${self.monto} realizado exitosamente.")

class Efectivo(MetodoPago):
    def __init__(self, monto, lugar):
        super().__init__(monto)
        self.lugar = lugar

    def pagar(self):
        print(f"Procesando pago en efectivo en {self.lugar}. Cobro de ${self.monto} realizado exitosamente.")

if __name__ == "__main__":
    pago_mp = MercadoPago(5000, "samuelcoky.mp")
    pago_nfc = NFC(1000, "Samsung A34")
    pago_debito = Debito(15000, "Galicia")
    pago_efectivo = Efectivo(6000, "Supermercado")

    pago_mp.pagar()
    pago_nfc.pagar()
    pago_debito.pagar()
    pago_efectivo.pagar()