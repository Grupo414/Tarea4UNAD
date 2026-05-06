#Modulo de gestion de reservas
#Integra cliente y servicio con manejo de excepciones y logs

from excepciones import ErrorReservaInvalida, ErrorServicioNoDisponible
from logs import registrar_log


class Reserva:

    # Constructor de la clase Reserva
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    # Método para confirmar la reserva
    def confirmar(self):
        try:
            # Validar que la duración sea correcta
            if self.duracion <= 0:
                raise ErrorReservaInvalida("Duración inválida")

            # Validar que exista un servicio
            if self.servicio is None:
                raise ErrorServicioNoDisponible("No hay servicio asignado")

            # Calcular el costo total de la reserva
            costo = self.servicio.calcular_costo() * self.duracion

        except ErrorReservaInvalida as e:
            # Manejo de error de duración inválida
            self.estado = "fallida"
            registrar_log(f"Reserva inválida: {e}")

        except ErrorServicioNoDisponible as e:
            # Manejo de error por servicio inexistente
            self.estado = "fallida"
            registrar_log(f"Servicio no disponible: {e}")

        except Exception as e:
            # Captura de cualquier error inesperado
            self.estado = "fallida"
            registrar_log(f"Error inesperado: {e}")

        else:
            # Se ejecuta si no hay errores
            self.estado = "confirmada"
            print(f"Reserva confirmada para {self.cliente.get_nombre()}")
            print(f"Costo total: {costo}")

        finally:
            # Siempre se registra el estado final
            registrar_log(f"Estado final de reserva: {self.estado}")

    # Método para cancelar la reserva
    def cancelar(self):
        try:
            # Validar que la reserva esté confirmada antes de cancelar
            if self.estado != "confirmada":
                raise ErrorReservaInvalida("No se puede cancelar una reserva no confirmada")

            self.estado = "cancelada"

        except Exception as e:
            # Registrar error en caso de fallo
            registrar_log(f"Error al cancelar: {e}")

        else:
            print("Reserva cancelada correctamente")

        finally:
            # Registrar intento de cancelación
            registrar_log("Intento de cancelación procesado")
