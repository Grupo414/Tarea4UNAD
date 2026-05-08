
# Proyecto: Sistema Integral de Gestión de Clientes
# Curso: Programación 213023
# Integrante:  Nini Johana Guerrero

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