import re, os, sys
"""
Script valido que formatea el output del comando oc.

"""



#archivo a utilizar
filename = "project_ocp.txt"

#chequea que el archivo exista
if not os.path.exists(filename):
    print("El archivo con información de los namesace no existe")
    sys.exit()

with open(filename,'r') as infile:
    lines = infile.readlines()

#imprime las lineas que machean
pattern = "(Name:|Namespace:|Resource|cpu|memory)"

with open("outfile.txt", "w") as outfile:
    for linea in lines:
        match = re.match(pattern,linea, re.IGNORECASE)
        if match:
            #print(linea)
            #newline = re.sub(pattern, linea)
            outfile.write(linea)
        