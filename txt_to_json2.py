import json, re
#from typing import Mapping

file = "outfile.txt"

#crea diccionario
dict={}

#create fieds to map with date in file
mappings = [ 'Name2' ]

#abrir archivo
with open(file) as fn:
    id = 1
    for d in fn:
        line = list(re.split("\s+", d.strip()))
        if "Resource" in line[0]:
            dict[line[0]] = {"Used": {}, "Hard": {}}
        elif "cpu" in line[0]:
            dict["Resource"]["Used"][line[0]] = re.findall("\d+",line[1])[0]
            dict["Resource"]["Hard"][line[0]] = re.findall("\d+",line[-1])[0]
        elif "memory" in line[0]:
            dict["Resource"]["Used"][line[0]] = re.findall("\d+",line[1])[0]
            dict["Resource"]["Hard"][line[0]] = re.findall("\d+",line[-1])[0]
        else:
            dict[line[0]] = line[-1]

        
        #intermediate dict to put fie data
        #dict2 = {}
       # while i < len(mappings):
        #    dict2[mappings[i]] =desc[i]
        #    i += 1
        #append person data to idoutfile
        #dict[person] = dict2
        id +=  1

#create output file
otfile = open("salida.json", "w")

json.dump(dict, otfile,indent=3)
otfile.close()
