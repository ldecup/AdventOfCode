import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

targetInput = "testinput.txt"

logger.info(f"Running on {targetInput}")
inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      targetInput)
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n'))
logger.info(f"Successfully imported {len(data)} lines of data")

nextVal = {'X':'M','M':'A','A':'S','S':'done'}
XMASList = []

def checkNextStep(data,line,col,currValue,dir):
    if dir == "N":
        try:
            if data[line-1][col] == nextVal[currValue]:
                checkNextStep(data,line,col,nextVal[currValue],dir)
                return nextVal[currValue]
        except:
            return False
    if dir == "NE":
        try:
            if data[line-1][col+1] == nextVal[currValue]:
                return nextVal[currValue]
            else: return False
        except:
            return False
    if dir == "E":
        try:
            if data[line][col+1] == nextVal[currValue]:
                return nextVal[currValue]
            else: return False
        except:
            return False
    if dir == "SE":
        try:
            if data[line+1][col+1] == nextVal[currValue]:
                return nextVal[currValue]
            else: return False
        except:
            return False
    if dir == "S":
        try:
            if data[line+1][col] == nextVal[currValue]:
                return nextVal[currValue]
        except:
            return False
    if dir == "SW":
        try:
            if data[line+1][col-1] == nextVal[currValue]:
                return nextVal[currValue]
        except:
            return False
    if dir == "W":
        try:
            if data[line][col-1] == nextVal[currValue]:
                return nextVal[currValue]
        except:
            return False
    if dir == "NW":
        try:
            if data[line-1][col-1] == nextVal[currValue]:
                return nextVal[currValue]
        except:
            return False

for line, lineIndex in enumerate(data):
    for char, charIndex in enumerate(line):
        if char == 'X':
            if data[lineIndex-1][charIndex] == 'M':
                