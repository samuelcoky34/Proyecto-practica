class MetodoPago:
    def __init__(self):
        self.__metodos = ["Efectivo", "Debito", "Mercado Pago", "NFC"]

    def mostrar_pagos(self):
        for opcion in self.__metodos:
            print(f"- {opcion}")

    def agregar_metodo(self, nuevo_metodo):
        if nuevo_metodo not in self.__metodos:
            self.__metodos.append(nuevo_metodo)
            print(f"Se añadio un nuevo método: {nuevo_metodo}")
        else:
            print(f"El método {nuevo_metodo} ya existe en la lista")

if __name__ == "__main__":
    pagos = MetodoPago()

    print("-- Listas inicial de métodos: ")
    pagos.mostrar_pagos()

    print("\n2. Agregando un nuevo método nuevo: ")
    pagos.agregar_metodo("Credito")

    print("\n3. Agregando un duplicado: ")
    pagos.agregar_metodo("Efectivo")

    print("\n4. Lista final actualizado: ")
    pagos.mostrar_pagos()