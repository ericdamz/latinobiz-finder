import csv
import os

DATA_FILE = "data/resultados.csv"

def cargar_datos_existentes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def guardar_resultados_nuevos(nuevos_resultados):
    existentes = cargar_datos_existentes()
    existentes_tuplas = {(x[0], x[1]) for x in existentes}
    nuevos_unicos = [fila for fila in nuevos_resultados if (fila[0], fila[1]) not in existentes_tuplas]
    if not nuevos_unicos:
        return 0
    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(nuevos_unicos)
    return len(nuevos_unicos)

def actualizar_estado_contacto(nombre, telefono, nuevo_estado):
    data = cargar_datos_existentes()
    actualizado = []
    for fila in data:
        if fila[0] == nombre and fila[1] == telefono:
            fila[5] = nuevo_estado
        actualizado.append(fila)
    with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(actualizado)
