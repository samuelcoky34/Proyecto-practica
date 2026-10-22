class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_productos(self):
        contandor = 1
        while True:
            producto = input("Introduce el nombre del producto por favor: ")
            precio = float(input("Introduce el precio del producto por favor: "))
            cantidad = float(input("Introduce la cantidad del producto por favor: "))

            self.productos.append({
                "Producto": producto,
                "Cantidad": cantidad,
                "Precio": precio
            })

            contandor += 1

            pregunta = input("¿Quieres agregar mas productos? (si/no) ").lower()
            if pregunta == "si":
                print("Continuemos")
            else:
                break

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            precio = producto["Precio"]
            cantidad = producto["Cantidad"]
            total += precio * cantidad
        return total

    def mostrar_resultado(self):
        pago = input("¿Con qué metodo de pago vas a utilizar?: ")
        print("--- TICKET DE COMPRA ---")
        for producto in self.productos:
            print(producto["Producto"])
            print(producto["Cantidad"])
            print(producto["Precio"])

        total_final = self.calcular_total()
        print(f"Metódo de pago: {pago}")
        print(f"TOTAL A PAGAR: {total_final}")

if __name__ == "__main__":
    mi_carrito = Carrito()
    mi_carrito.agregar_productos()
    mi_carrito.mostrar_resultado()