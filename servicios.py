# Modulo para herencia y Poliformismo
from abc import ABC, abstractmethod
from excepciones import ErrorValidacionDatos

# CLASE ABSTRACTA

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, duracion, **kwargs):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

# CLASES HIJAS - Herencia y Polimorfismo

class ReservaSala(Servicio):
    def __init__(self, capacidad):
        super().__init__("Reserva de Sala", 50000)
        self.capacidad = capacidad

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorValidacionDatos("La duración debe ser mayor a 0")
        # Polimorfismo: Recargo por capacidad
        recargo = 10000 if self.capacidad > 10 else 0
        return (self._costo_base + recargo) * horas

    def describir_servicio(self):
        return f"Sala para {self.capacidad} personas."

class AlquilerEquipo(Servicio):
    def __init__(self, tipo_equipo):
        super().__init__("Alquiler de Equipo", 30000)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias, seguro=True):
        if dias <= 0:
            raise ErrorValidacionDatos("Los días deben ser mayores a 0")
        costo = self._costo_base * dias
        if seguro: costo += 5000 * dias
        return costo

    def describir_servicio(self):
        return f"Equipo: {self.tipo_equipo}"

class AsesoriaEspecializada(Servicio):
    def __init__(self, experto):
        super().__init__("Asesoría Especializada", 80000)
        self.experto = experto

    def calcular_costo(self, horas, prioridad="normal"):
        if horas <= 0:
            raise ErrorValidacionDatos("Horas de asesoría inválidas")
        multiplicador = 1.5 if prioridad == "urgente" else 1.0
        return (self._costo_base * horas) * multiplicador

    def describir_servicio(self):
        return f"Asesoría técnica con {self.experto}"