# holaaaa 

# Hola compañeros, de acuerdo con mi consulta para el desarrollo del codigo es importante que importemos las librerias de datatime y abc 
# para que el codigo sea organizado y para que que python no vea las fechas como solo texto si no que asi se conviertan en objetos inteligentes
import datetime
import abc
# Creamos las siguientes clases para generar alertas en el momento que presentemos un error y asi poder identificarlo
class ErrorSoftwareFJ(Exception):
    """Clase madre para todos los errores de nuestra empresa."""
    pass
class ErrorValidacionDatos(ErrorSoftwareFJ):
    """Se usa cuando un dato como la cédula o días es inválido."""
    pass
class ErrorReservaInvalida(ErrorSoftwareFJ):
    """Se usa cuando la lógica de negocio no se cumple (ej. costo 0)."""
    pass

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