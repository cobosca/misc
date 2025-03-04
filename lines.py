import sys

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    filename = sys.argv[1]
    del_lines = []

if not filename.endswith(".py"):
    sys.exit("Not a python file")
    
try: 
    with open(filename, "r") as file:
        lines = file.readlines()
except:
    sys.exit("File not found")
    
for line in range(0, len(lines)):
    if lines[line][0] == "#":
        del_lines.append(line)
        
for line in range(0, len(del_lines)):
    del lines[line]

print(len(lines))
