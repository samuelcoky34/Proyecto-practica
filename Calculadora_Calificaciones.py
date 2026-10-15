class CalculadoraNotas:
    def __init__(self):
        self.notas = []

    def pedir_nota(self, posicion):
        while True:
            try:
                nota = float(input(f"Introduce la {posicion} entre (1 al 10) por favor para calcular el promedio de notas: "))
                if 1 <= nota <= 10:
                    self.notas.append(nota)
                    break
                else:
                    print("La nota debe ser entre 1 al 10. Intentalo de nuevo por favor")
            except ValueError:
                print("Error: Ingesaste texto de cadena o numero flotantes. Tienes que poner numero entero (int)")

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def mostrar_resultado(self):
        resultado = self.calcular_promedio()
        print(f"\nEl resultado final es {resultado:.2f}")

if __name__ == "__main__":
    calculadora = CalculadoraNotas()

    calculadora.pedir_nota("Primera")
    calculadora.pedir_nota("Segunda")
    calculadora.pedir_nota("Tercera")
    calculadora.pedir_nota("Cuarta")
    calculadora.pedir_nota("Quinta")

    calculadora.mostrar_resultado()