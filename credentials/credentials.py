import os.path


keyVars = ['consumerKey', 'consumerSecret', 'accessToken', 'accessSecret']
availablekeys = []

def errorOutput(lines):
    for line in lines:
        s = line.split()
        if len(s) > 0:
            k = s[0]
            availablekeys.append(k)

    missing = list(set(keyVars) - set(availablekeys))
    print 'You\'re missing the following credential keys: '
    for m in missing:
        print m

def checkForKeys():
    fname = 'credentials/keys.txt'
    print 'here'
    global keyVals
    keyVals = {}
    if os.path.isfile(fname):
        with open(fname) as f:
            lines = f.readlines()

            for line in lines:
                s = line.split()
                keyVals[s[0]] = s[2]
                if len(line.split()) < 1:
                    errorOutput(lines)
                    break
    else:
        target = open(fname, 'w')
        
        consumerKey = raw_input('Enter \'consumerKey\': ')
        target.write('consumerKey = ' + consumerKey + '\n')
        keyVals['consumerKey'] = consumerKey

        consumerSecret = raw_input('Enter \'consumerSecret\': ')
        target.write('consumerSecret = ' + consumerSecret + '\n')
        keyVals['consumerSecret'] = consumerSecret

        accessToken = raw_input('Enter \'accessToken\': ')
        target.write('accessToken = ' + accessToken + '\n')
        keyVals['accessToken'] = accessToken

        accessSecret = raw_input('Enter \'accessSecret\': ')
        target.write('accessSecret = ' + accessSecret + '\n')
        keyVals['accessSecret'] = accessSecret

        target.close()



def getConsumerKey():
    checkForKeys()
    return keyVals['consumerKey']

def getConsumerSecret():
    checkForKeys()
    return keyVals['consumerSecret']

def getAccessToken():
    checkForKeys()
    return keyVals['accessToken']

def getAccessSecret():
    checkForKeys()
    return keyVals['accessSecret']
