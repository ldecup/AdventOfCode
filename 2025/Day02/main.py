import os
import logging

def hasRangeInvalidIDs(testedRange):
    invalidIDSum = 0
    for i in range(int(testedRange[0]), int(testedRange[1]) + 1):
        if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
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

    totalInvalidIDs = 0

    data = inData[0].rstrip('\n').split(",")
    for index, datum in enumerate(data):
        data[index] = datum.split("-")
        totalInvalidIDs += hasRangeInvalidIDs(data[index])

    logger.info(f"Total sum of invalid IDs: {totalInvalidIDs}")

if __name__ == "__main__":
    main()