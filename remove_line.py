#import fileinput
#import sys
#
#for line_number, line in enumerate (fileinput.input('project_ocp.txt', inplace=1)):
#    if len(line) > 1:
#        sys.stdout.write(line)
#
#otfile = open("sexit.json", "w")
#otfile.close()

file = 'project_ocp.txt'

#elimina la linea que contiene Scopes
with open(file,"r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if ('\n') not in line:
            f.write(line)
    f.truncate()
