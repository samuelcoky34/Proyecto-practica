class CajaMonedero:
    def __init__(self):
        self.__caja = 0

    def cobrar(self, total):
        if total > 0:
            self.__caja += total
            print(f"Cobro exitoso el cobro es: ${total:.2f}")
        else:
            print("Error: El monto debe ser mayor a cero y la caja no se toca")

    def ver_caja(self):
        print(f"Total de la caja es: {self.__caja:.2f}")

if __name__ == "__main__":
    caja = CajaMonedero()
    while True:
        print("\n--- CAJA SISTEMA ---")
        print("1. Cobrar")
        print("2. Ver caja")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                try:
                    monto = float(input("Ingrese al monto a cobrar: "))
                    caja.cobrar(monto)
                except ValueError:
                    print("Ingresaste un valor que no corresponde. Vuelve a intentarlo")
            case "2":
                caja.ver_caja()
            case "3":
                print("Saliendo de la caja ...")
                break
            case _:
                print("Opción invalida. Selecciona de las opciones del (1 al 3)")