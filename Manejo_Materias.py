class MateriasNotas:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        self.notas = []

    def pedir_notas(self, posicion):
        while True:
            try:
                nota = float(input(f"Introduce la {posicion} entre (1 al 10) Por favor: "))
                if 1 <= nota <= 10:
                    self.notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1 y 10. Por favor vuelve a intentarlo.")
            except ValueError:
                print("Error: Ingresaste un formato inválido. Debe ser un número entero o decimal (ej: 8 o 9.5).")

    def calcular_promedio(self):
        if not self.notas:
            return 0
        promedio = sum(self.notas) / len(self.notas)
        return promedio

    def mostrar_resultados(self):
        resultado = self.calcular_promedio()
        print(f"\nEl alumno {self.nombre} en la materia {self.materia}. El resultado total es {resultado:.2f}")
        if resultado >= 7:
            print("Aprobado")
        else:
            print("Desaprobado")

if __name__ == "__main__":
    alumno1 = MateriasNotas("Samuel", "Matemáticas")
    alumno1.pedir_notas("primera")
    alumno1.pedir_notas("segunda")
    alumno1.mostrar_resultados()

    alumno1 = MateriasNotas("Brian", "Filosofia")
    alumno1.pedir_notas("primera")
    alumno1.pedir_notas("segunda")
    alumno1.mostrar_resultados()