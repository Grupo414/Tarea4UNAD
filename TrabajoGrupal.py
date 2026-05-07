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