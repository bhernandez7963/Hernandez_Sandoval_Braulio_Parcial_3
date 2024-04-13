import json

# Nombre del archivo JSON
nombre_archivo = "file.json"

# Cargar el JSON desde el archivo
with open(nombre_archivo, 'r') as archivo:
    data = json.load(archivo)

# Imprimir el JSON cargado
print(data["ip"] + "\n" + data["so"] + "\n" + data["version"][0] + "\n" + data["hostname"] + "\n" + data["cpu"])
