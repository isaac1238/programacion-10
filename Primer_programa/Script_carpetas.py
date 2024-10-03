# Rutas y archivos
import os
import shutil

# Tiempo
import time

# Funcion que retorna el string de la fecha de creacion de un archivo
# Recibe la ruta del archivo
def obtener_fecha_creacion(ruta_archivo):

    timestamp_creacion = os.path.getctime(ruta_archivo) # Obtiene el timestamp de creacion (since epoch)

    # Formato YYYY-MM-DD
    return time.strftime('%Y-%m-%d', time.localtime(timestamp_creacion))

# Organiza los archivos en subcarpetas segun su extension y agrega
# la fecha de creacion al inicio del nombre de cada archivo.
def organizar_archivos_por_extension(directorio):
    
    # Revisar que el directorio a organizar exista
    if not os.path.isdir(directorio):
        print(f"El directorio {directorio} no existe.")
        return
    
    # Recorrer elementos en el directorio
    for archivo in os.listdir(directorio):
        # Ruta de archivo = Ruta carpeta + nombre de archivo
        # ./directorioEjemplo/archivo
        ruta_archivo = os.path.join(directorio, archivo)

        # Verifica que sea un archivo y no un directorio
        if os.path.isfile(ruta_archivo):
            # Obtiene la extension del archivo
            extension = archivo.split('.')[-1]

            # Crea la carpeta con el nombre de extension si no existe
            # Ej1: ./directorioEjemplo/txt/
            # Ej2: ./directorioEjemplo/py/
            carpeta_extension = os.path.join(directorio, extension)

            # Si no existe la carpeta, se crea
            if not os.path.exists(carpeta_extension):
                os.makedirs(carpeta_extension)
            
            # Obtiene la fecha de creacion del archivo
            fecha_creacion = obtener_fecha_creacion(ruta_archivo)
            
            # Crea el nuevo nombre del archivo con la fecha
            nuevo_nombre = f"{fecha_creacion}_{archivo}"
            nueva_ruta = os.path.join(carpeta_extension, nuevo_nombre) # directorio/extension/nuevo_nombre
            
            # Mueve el archivo a la nueva carpeta con el nuevo nombre
            shutil.move(ruta_archivo, nueva_ruta)
            # Viejo: ./directorioEjemplo/texto.txt
            # Nuevo: ./directorioEjemplo/txt/2024-09-18_texto.txt

            print(f"Movido: {archivo} -> {nueva_ruta}")
        else:
            print(f"Saltando directorio: {archivo}")

# Ruta al directorio que deseas organizar
directorio_a_organizar = 'directorioEjemplo'

# Llama a la función para organizar los archivos
organizar_archivos_por_extension(directorio_a_organizar)