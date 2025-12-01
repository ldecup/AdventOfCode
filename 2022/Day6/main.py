inFile = open('Day6/input.txt', 'r')
dataStream = inFile.readlines()[0]
inFile.close()

datagramList = []
for i in range(4,len(dataStream)):
    datagram = dataStream[i-4:i]
    isDatagramValid = True
    for char in datagram:
        if datagram.count(char) > 1:
            isDatagramValid = False
    if isDatagramValid:
        datagramList.append([i,datagram])

print(datagramList)