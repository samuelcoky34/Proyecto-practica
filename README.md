# Practicas de Python y POO

Ejercicios de programación en Python, destacando `practica_poo_completa.py` (simulador de pagos con `Efectivo`, `Credito`, `Debito`, `NFC` y `MercadoPago`).

## Pilares de POO en `practica_poo_completa.py`

- **Abstracción:** `MetodoPago(ABC)` y `@abstractmethod def pagar()`.
- **Encapsulamiento:** `self.__monto` y `obtener_monto()`.
- **Herencia:** Clases hijas con `super().__init__(monto)`.
- **Polimorfismo:** Bucle `for` ejecutando `.pagar()` sin `if`.

## Ejecución

```bash
python practica_poo_completa.py
```
