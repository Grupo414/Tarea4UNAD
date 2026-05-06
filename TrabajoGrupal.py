# Archivo principal para probar el sistema
# Se ejecutan casos válidos e inválidos

from cliente import Cliente
from servicios import ReservaSala
from reserva import Reserva
from excepciones import ErrorSoftwareFJ
from logs import registrar_log


def simulacion():
    try:
        # Caso válido
        cliente1 = Cliente("Juan", "123")
        servicio1 = ReservaSala(2)

        reserva1 = Reserva(cliente1, servicio1, 2)
        reserva1.confirmar()

        # Caso inválido: duración negativa
        reserva2 = Reserva(cliente1, servicio1, -1)
        reserva2.confirmar()

        # Caso inválido: cliente incorrecto
        cliente2 = Cliente("", "abc")

    except ErrorSoftwareFJ as e:
        # Manejo de errores generales del sistema
        registrar_log(f"Error general del sistema: {e}")

    finally:
        # Indica que la simulación terminó
        print("Simulación finalizada")


simulacion()