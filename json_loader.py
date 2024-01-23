import json

def cargar_datos_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombre_archivo}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")
        return None

# Uso de la función para cargar datos desde un archivo JSON
nombre_archivo = "nombres.json"  # Reemplaza con el nombre real de tu archivo JSON
datos = cargar_datos_desde_archivo(nombre_archivo)

if datos and "listadoNombres" in datos:
    # Acceder a los datos cargados
    listado_nombres = datos["listadoNombres"]

    # Imprimir algunos datos como ejemplo
    print("Nombres:")
    for nombre_info in listado_nombres:
        print(nombre_info["nombre"], " - Sexo:", "Mujer" if nombre_info["sexo"] else "Hombre")
else:
    print("No se cargaron datos desde el archivo.")

