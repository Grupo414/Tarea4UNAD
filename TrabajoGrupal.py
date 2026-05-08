

# cliente.py
from abc import ABC, abstractmethod

# Clase abstracta base
class Entidad(ABC):
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        pass


# Clase Cliente
class Cliente(Entidad):
    def __init__(self, id, nombre, correo):
        super().__init__(id, nombre)
        self._correo = correo
        self.validar_datos()

    def validar_datos(self):
        if not self._nombre or self._nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in self._correo or "." not in self._correo:
            raise ValueError("Correo inválido")

    def mostrar_info(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Correo: {self._correo}"


# Lista de clientes
clientes = []


# Función para agregar clientes
def agregar_cliente(id, nombre, correo):
    try:
        cliente = Cliente(id, nombre, correo)
        clientes.append(cliente)
        print("Cliente agregado correctamente")

    except ValueError as e:
        print("Error al crear cliente:", e)


# PRUEBAS
if __name__ == "__main__":

    # Cliente válido
    agregar_cliente(1, "Johana", "johana@email.com")

    # Cliente inválido
    agregar_cliente(2, "", "correo_malo")

    # Mostrar clientes guardados
    for c in clientes:
        print(c.mostrar_info())

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
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorSoftwareFJ
from logs import registrar_log


def simulacion():
    try:
        # Caso válido
        cliente1 = Cliente("Juan", "123", 'juan@gmail.com')
        servicio1 = ReservaSala(2)

        reserva1 = Reserva(cliente1, servicio1, 2)
        reserva1.confirmar()

        # Caso inválido: duración negativa
        reserva2 = Reserva(cliente1, servicio1, -1)
        reserva2.confirmar()

        # Caso inválido: cliente incorrecto
        cliente2 = Cliente("", "abc", "correo@gmail.com")

    except ErrorSoftwareFJ as e:
        # Manejo de errores generales del sistema
        registrar_log(f"Error general del sistema: {e}")

    finally:
        # Indica que la simulación terminó
        print("Simulación finalizada")


simulacion()

