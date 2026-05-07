#Excepciones 
class ErrorSoftwareFJ(Exception):
    """Clase base para errores del sistema"""
    pass


class ErrorValidacionDatos(ErrorSoftwareFJ):
    """Datos inválidos"""
    pass


class ErrorReservaInvalida(ErrorSoftwareFJ):
    """Errores en la lógica de reservas"""
    pass


class ErrorServicioNoDisponible(ErrorSoftwareFJ):
    """Servicio no disponible"""
    pass