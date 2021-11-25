from os import O_TMPFILE


file = 'project_ocp.txt'

with open(file, 'r+') as f:
    old = f.read() # read everything in the file
      # write the new line before
otfile = open("fuera.txt", "w")

otfile.close()