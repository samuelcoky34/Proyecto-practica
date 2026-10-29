class CajaMonedero:
    def __init__(self):
        self.__caja = 0

    def cobrar(self, total):
        if total > 0:
            self.__caja += total
            print(f"Cobro exitoso el cobro es: ${total}")
        else:
            print("Error: El monto debe ser mayor a cero y la caja no se toca")

    def ver_caja(self):
        print(f"Total de la caja es: {self.__caja}")

if __name__ == "__main__":
    caja = CajaMonedero()

    caja.cobrar(5000)
    caja.cobrar(-3000)
    caja.cobrar(1000)
    caja.ver_caja()
