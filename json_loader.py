import json, random

from rich.console import Console

console = Console()

# Lee el archivo JSON
with open('nombres.json', 'r') as file:
    data = json.load(file)

# Accede a la lista de nombres de hombres
nombres_hombres = data["nombres"]["hombre"]
nombres_mujeres = data["nombres"]["mujer"]
apellidos_chilenos = data["nombres"]["apellidos"]["chilenos"]
profeciones = data["nombres"]["profeciones"]

# Imprime los nombres de hombres
# print("Nombres de hombres:")
# for nombre in nombres_hombres:
    # print(nombre)

# for apellidos in apellidos_chilenos:
    # print(apellidos)

# for profecion in profeciones:
    # print(profecion)

# Impriemiendo elementos de forma aleatoria.
print(f"nombre: {''.join(random.choices(nombres_hombres))} apellido: {''.join(random.choices(apellidos_chilenos))}")

# Buscando un elemento.

elemento_a_buscar = "jaime"
if elemento_a_buscar in nombres_hombres:
    print(f"{elemento_a_buscar} está en la lista")
else:
    print(f"{elemento_a_buscar} no está en la lista")


# Buscando conincidencias.

print("[ Buscando coincidencias con 'ja' ]")

for nombre in nombres_hombres:
    if "ja" in nombre.lower():
        nombre_resaltado = nombre.lower().replace("ja", "[red]ja[/red]")
        console.print(nombre_resaltado)

