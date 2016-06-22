fname = "commonVerbs.txt"

with open(fname) as f:
    lines = f.readlines()

resultLines = ""
for line in lines:
    resultLines += line.lower()

file = open("commonVerbs.txt", "w")

file.write(resultLines)

file.close()
