# Calculadoras_Calificaciones - Versión Base

def pedir_notas(posicion):
    while True:
        nota = float(input(f"Introduce la {posicion} nota entre (1 a 10): "))
        if 1 <= nota <= 10:
            return nota
        print("La nota debe estar entre 1 al 10. Por favor vuelve a intentarlo")

nota1 = pedir_notas("primera")
nota2 = pedir_notas("segunda")
nota3 = pedir_notas("tercera")

promedio = (nota1 + nota2 + nota3) / 3

print(f"/nEl promedio total es: {promedio:.2f}")