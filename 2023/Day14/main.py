import os
import re

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'testinput.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

rockMap = []
for line in inData:
    rockMap.append(line.rstrip('\n'))

def flipMap(rockMap):
    #Flips the map 90° anti-clockwise
    flippedMap = []
    for a in range(len(rockMap[0])):
        colAsLine = ''
        for line in rockMap:
            colAsLine += line[a]
        flippedMap.insert(0,colAsLine)
    return flippedMap

def rollLeft(rockMap):
    for line in rockMap:
        hRocks = []
        for match in re.finditer(r'#', line):
            hRocks.append(match.start())
        for a in range(len(hRocks)):
            segment = list(line)[hRocks[a]:hRocks[a+1]]

rockMap = rollLeft(flipMap(rockMap))

print("done")