
# trabajo colaborativo 
from abc import ABC, abstractmethod

# Clase abstracta
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
        if not self._nombre:
            raise ValueError("El nombre no puede estar vacío")
        if "@" not in self._correo:
            raise ValueError("Correo inválido")

    def mostrar_info(self):
        return f"Cliente: {self._nombre}, Correo: {self._correo}"


# Lista de clientes
clientes = []

# Pruebas
try:
    c1 = Cliente(1, "Johana", "johana@email.com")
    clientes.append(c1)
    print(c1.mostrar_info())
except Exception as e:
    print("Error:", e)

try:
    c2 = Cliente(2, "", "correo_malo")
    clientes.append(c2)
except Exception as e:
    print("Error:", e)