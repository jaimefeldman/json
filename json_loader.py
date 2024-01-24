import json

# Lee el archivo JSON
with open('nombres.json', 'r') as file:
    data = json.load(file)

# Accede a la lista de nombres de hombres
nombres_hombres = data["nombres"]["hombre"]
nombres_mujeres = data["nombres"]["mujer"]
apellidos_chilenos = data["nombres"]["apellidos"]["chilenos"]
profeciones = data["nombres"]["profeciones"]

# Imprime los nombres de hombres
print("Nombres de hombres:")
for nombre in nombres_hombres:
    print(nombre)

for apellidos in apellidos_chilenos:
    print(apellidos)

for profecion in profeciones:
    print(profecion)
