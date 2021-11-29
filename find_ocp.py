import re, os, sys
"""
Script valido para formatear el output del comando oc.
comando oc:
oc describe quota  --all-namespaces
"""

## ejecutar el comando de oc para generar el archivo project_ocp.txt
#oc describe quota  --all-namespaces > /home/appdynamics/ocp_get_pods/scripts/project_ocp.txt

ruta_testing = "/home/appdynamics/ocp_get_pods/scripts/testing_ocp/"
out_testing = ruta_testing + "etl_output_testing.txt"

#archivo a utilizar
filename = ruta_testing + "all_namespaces_quota.txt"

#chequea que el archivo exista
if not os.path.exists(filename):
    print("El archivo con información de los namespace no existe")
    sys.exit()

with open(filename,'r') as infile:
    lines = infile.readlines()

#imprime las lineas que machean
pattern = "(Name:|Namespace:|Resource|cpu|memory)"

with open(out_testing, "w") as outfile:
    swicht = True 
    for linea in lines:
        if re.findall("(burst)", linea,re.IGNORECASE):
            swicht = False
        elif re.findall("(quota)", linea, re.IGNORECASE):
            swicht = True
        if swicht:
            match = re.match(pattern,linea, re.IGNORECASE)
            if match:
            #print(linea)
            #newline = re.sub(pattern, linea)
                outfile.write(linea)
