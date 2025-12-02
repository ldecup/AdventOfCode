import os
import logging

def main():
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    logger = logging.getLogger(__name__)

    mainInput = "input.txt"
    testInput = "testinput.txt"
    txtInput = testInput

    logger.info(f"Running on {txtInput}")
    inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        txtInput)
    inFile = open(inPath, 'r')
    inData = inFile.readlines()
    inFile.close()

    data = []
    for line in inData:
        data.append(line.rstrip('\n'))
    logger.info(f"Successfully imported {len(data)} lines of data")

if __name__ == "__main__":
    main()