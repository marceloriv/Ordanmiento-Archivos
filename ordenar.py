import os
import shutil

def organizar_archivos_por_extension(directorio):
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

# Ejemplo de uso
directorio = '/ruta/del/directorio'  # Cambiar por el directorio deseado
organizar_archivos_por_extension(directorio)
