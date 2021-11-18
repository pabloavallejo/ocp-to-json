import json
from typing import Mapping

file = "ejemplo1.txt"

#crea diccionario
dict={}

#create fieds to map with date in file
mappings = ['name', 'gender']

#abrir archivo

with open(file) as fn:
    id = 1
    for d in fn:
        desc = list(d.strip().split(' ',1))
        #i am taking person name as id
        person = desc[0]
        i = 0
        #intermediate dict to put fie data
        dict2 = {}
        while i < len(mappings):
            dict2[mappings[i]] =desc[i]
            i = i + 1

        #append person data to id
        dict[person] = dict2
        id = id +1

#create output file
otfile = open("salida.json", "w")
json.dump(dict, otfile,indent=3)
otfile.close()