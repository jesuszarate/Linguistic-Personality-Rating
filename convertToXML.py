fname = "parsedTable.txt"
kfname = "keywords.txt"
cfname = "categories.txt"

with open(fname) as f:
    lines = f.readlines()

with open(kfname) as kf:
    klines = kf.readlines()

with open(cfname) as cf:
    clines = cf.readlines()

ratings = ["Na", "Ma", "Ps", "Op", "Co", "Ex", "Ag", "Ne"]

def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

resultXML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
resultXML += "<pesonality_scores>\n"
keywordInd = 0;


#for line in lines:
for x in range(0, len(lines)):
    s = lines[x].split()
    cat = clines[x]

    isAbbrev = False
    resultXML += "<entry>\n"
    print "<entry>"

    rtngInd = 0
    for i in range(0, len(s)):
        word = s[i]
        if ((is_float_try(word)) == False):
            print "<category>" + cat + "</category>"
            print "<abbrev>" + word + "</abbrev>"
            resultXML += "<category>" + cat.rstrip() + "</category>\n"
            resultXML += "<abbrev>" + word + "</abbrev>\n"
            if(isAbbrev == False):
                print "<ratings>"
                resultXML += "<ratings>\n"
                isAbbrev = True
        else:
            print "<" + ratings[rtngInd] + ">" + word + "</" + ratings[rtngInd] + ">"
            resultXML += "<" + ratings[rtngInd] + ">" + word + "</" + ratings[rtngInd] + ">\n"
            rtngInd = rtngInd + 1            

    print "</ratings>"
    resultXML += "</ratings>\n"

    resultXML = resultXML + "<keywords>\n" + klines[keywordInd] + "</keywords>\n"
    keywordInd += 1;
    print "<keywords></keywords>"
    print "</entry>"
    resultXML += "</entry>\n"
    print "\n\n"
    resultXML += "\n\n"


resultXML += "</pesonality_scores>"
file = open("ratings.xml", "w")
file.write(resultXML)
file.close()
