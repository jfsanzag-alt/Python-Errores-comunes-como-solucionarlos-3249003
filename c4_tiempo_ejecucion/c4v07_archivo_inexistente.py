import csv

#with open("/workspaces/Python-Errores-comunes-como-solucionarlos-3249003/c4_tiempo_ejecucion/archivos/datos.csv", "r", encoding="UTF-8") as archivo:
with open("c4_tiempo_ejecucion/archivos/datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    columnas = next(reader)
    for fila in reader:
        print(fila[0])

import os

ruta_actual = os.getcwd()
print(f"Estás trabajando en: {ruta_actual}")

# Ruta completa al archivo
ruta_archivo = os.path.abspath(__file__)

# Solo la carpeta que contiene al archivo
directorio_script = os.path.dirname(ruta_archivo)

print(f"El archivo está en: {ruta_archivo}")
print(f"La carpeta del script es: {directorio_script}")

import sys

print(f"El ejecutable de Python es: {sys.executable}")