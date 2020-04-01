def toDict(filename):
    f = open(filename, 'r')
    myDict = {}
    for line in f:
        k, v = line.strip().split(":")
        myDict[k.strip()] = v.strip()
    f.close()
    return myDict