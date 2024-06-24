

import json

def cargar_datos(archivo):
    dato = open(archivo, 'r')
    datos = json.load(dato)
    return datos

json
def guardar_datos():
    dato = open()
    json.dump(datos, dato, indent=4)

def agregar_libro(archivo, nuevoLibro):
    datos = cargar_datos(archivo)
    datos.append(nuevoLibro)
    guardar_datos(archivo, datos)

def editar_libro(archivo, libroID, NuevaInfo):
    datos = cargar_datos(archivo)
    for libro in datos:
        if libro['ID'] == libroID:
            libro.update(nueva_info):
            break
    guardar_datos(archivo,datos)

def eliminar_libro(archivo, libroID):
    datos = cargar_datos(archivo)
    datos = [libro for libro in datos if libro['ID'] != libroID]
    guardar_datos(archivo, datos)

def buscar_libro(archivo,libroID):
    datos = cargar_datos(archivo)
    for libro in datos:
        if libro['ID'] == libroID:
            return libro
        
def generar_reporte(archivo, reporte_archivo):
    datos = cargar_datos(archivo)
    prestamo = [libro for libro in datos if 'prestado' in libro]
    if prestamo:
        libro_mas_pedido = max(prestamo),
    key = lambda x: x.get('veces prestado',0)
    else:

