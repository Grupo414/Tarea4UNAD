
from datetime import datetime

def registrar_log(mensaje):
    with open("log.txt", "a", encoding="utf-8") as archivo:
        
        #Obtiene la fecha y hora actual
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] {mensaje}\n")
        