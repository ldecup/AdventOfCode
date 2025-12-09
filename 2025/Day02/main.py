import os
import logging
import re

def hasRangeInvalidIDsP1(testedRange):
    invalidIDSum = 0
    for i in range(int(testedRange[0]), int(testedRange[1]) + 1):
        if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
            invalidIDSum += i
    return invalidIDSum

def hasRangeInvalidIDsP2(testedRange):
    regexp2 = r"^(\d+)\1+$" #Look for a pattern of 1 or more digits, that repeat, at least once, spanning between the start and the end of the string
    invalidIDSum = 0
    for i in range(int(testedRange[0]), int(testedRange[1]) + 1):
        if len(re.findall(regexp2,str(i))) != 0:
            invalidIDSum += i
    return invalidIDSum

def main():
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    logger = logging.getLogger(__name__)

    mainInput = "input.txt"
    testInput = "testinput.txt"
    txtInput = mainInput

    logger.info(f"Running on {txtInput}")
    inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        txtInput)
    inFile = open(inPath, 'r')
    inData = inFile.readlines()
    inFile.close()

    totalInvalidIDsP1 = 0
    totalInvalidIDsP2 = 0

    data = inData[0].rstrip('\n').split(",")
    for index, datum in enumerate(data):
        data[index] = datum.split("-")
        totalInvalidIDsP1 += hasRangeInvalidIDsP1(data[index])
        totalInvalidIDsP2 += hasRangeInvalidIDsP2(data[index])

    logger.info(f"Total sum of invalid IDs for part 1: {totalInvalidIDsP1}")
    logger.info(f"Total sum of invalid IDs for part 2: {totalInvalidIDsP2}")

if __name__ == "__main__":
    main()