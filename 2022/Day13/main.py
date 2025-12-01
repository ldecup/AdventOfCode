inFile = open('Day13/testinput.txt', 'r')
inData = inFile.readlines()
inFile.close()

data = []
for index, line in enumerate(inData):
    if line == '\n':
        data.append([inData[index-2].rstrip('\n'),inData[index-1].rstrip('\n')])


def unpackPacket(packet):
    outPacket = []
    for index, char in enumerate(packet):
        if char == '[':
            backtrackIndex = 1
            while packet[-backtrackIndex] != ']':
                backtrackIndex += 1
            outPacket.append(packet[index+1:-backtrackIndex])
            packet = packet[:index+1] + packet[-backtrackIndex:]
            print(outPacket)

print(data[1][0])
unpackPacket(data[1][0])




