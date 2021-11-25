import json


#archivo a convertir
file = "project_ocp.txt"

#diccionario donde guarda los datos
dict = {}

#lee el archivo
with open(file) as fn:
    for d in fn: 
        #Lee el archivo y recorta espacios para obtener palabras validas
        key, desc = d.strip().split(None, 1)
        dict[key] = desc.strip()

#creado el diccionario, se crea la salida json
otfile = open("output1.txt","w")
json.dump(dict, otfile)
otfile.close()