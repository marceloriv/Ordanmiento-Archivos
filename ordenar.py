""" Script que organiza los archivos de un directorio por extensión. """

import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def organizar_archivos_por_extension(directorio):
    """Función que organiza los archivos de un directorio por extensión."""
    # Verificar si el directorio existe
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe.")
        return

    # Recorrer todos los archivos en el directorio
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)

        # Ignorar carpetas, solo trabajar con archivos
        if os.path.isfile(ruta_archivo):
            # Obtener la extensión del archivo
            extension = os.path.splitext(archivo)[1][1:]  # Quitar el punto (.)

            # Crear la carpeta si no existe
            carpeta_destino = os.path.join(directorio, extension)
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            # Mover el archivo a la carpeta correspondiente
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
            print(f"Movido: {archivo} -> {carpeta_destino}")
    messagebox.showinfo("Completo", "Se termino de ordenar los archivos")


def seleccionar_directorio():
    """Función que permite seleccionar un directorio mediante una interfaz gráfica."""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo("", "Seleccione el directorio a ordenar.")
    directorio = (
        filedialog.askdirectory()
    )  # Abrir cuadro de diálogo para seleccionar carpeta
    return directorio


# Ejemplo de uso con interfaz gráfica
directorio_seleccionado = seleccionar_directorio()
if directorio_seleccionado:
    organizar_archivos_por_extension(directorio_seleccionado)
else:
    messagebox.showinfo("Info", " No se selecciono un directorio")

version = "1.0.0"
