fname = 'f.txt'
fabs = 'Abbreviations.txt'

with open(fname) as f:
    lines = f.readlines()

with open(fabs) as f:
    abs = f.readlines()


def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

t = True
current = ""
i = 0
result = ""
for line in lines:

    s = line.split()

    for word in s:
        if(is_float_try(word)):
            current +=  ' ' + word

    print abs[i].split()[0] + current + "\n"
    result += abs[i].split()[0] + current + "\n"
    current = ""
    i = i + 1



file = open("parsedTable.txt", "w")

file.write(result)

file.close()

#print len(lines)
    #if searchtxt in line and i+1 < len(lines):
     #   print lines[i+1]        
