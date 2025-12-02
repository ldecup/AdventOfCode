import os
import logging

incrementPosition = lambda currentPos, instruction: (currentPos + instruction - (100 if currentPos + instruction > 99 else 0), (1 if (currentPos + instruction > 99) and (currentPos != 0) else 0))
decrementPosition = lambda currentPos, instruction: (currentPos - instruction + (100 if currentPos - instruction < 0 else 0), (1 if (currentPos - instruction <= 0) and (currentPos != 0) else 0))

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

    currentPos = 50
    zeroCounter = 0
    wentPastZeroCounter = 0

    for line in inData:
        datum = line.rstrip('\n')
        fullTurns, instruction = divmod(int(datum[1:]), 100)
        wentPastZeroCounter += fullTurns
        if datum[0] == "R":
            currentPos, wentPastZero = incrementPosition(currentPos, instruction)
            logger.debug(f"Went right for {instruction}\tticks, newpos = {currentPos}\twent past zero: {fullTurns + wentPastZero}\ttime(s)")
        elif datum[0] == "L":
            currentPos, wentPastZero = decrementPosition(currentPos, instruction)
            logger.debug(f"Went left  for {instruction}\tticks, newpos = {currentPos}\twent past zero: {fullTurns + wentPastZero}\ttime(s)")
        if currentPos == 0:
            zeroCounter += 1
        wentPastZeroCounter += wentPastZero
    logger.info(f"Landed on zero {zeroCounter} times, went past zero {wentPastZeroCounter} times")

if __name__ == "__main__":
    main()