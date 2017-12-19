
def toBinary(num):
    if num == 0:
        return "0000"
    elif num == 1:
        return "0001"
    elif num == 2:
        return "0010"
    elif num == 3:
        return "0011"
    elif num == 4:
        return "0100"
    elif num == 5:
        return "0101"
    elif num == 6:
        return "0110"
    elif num == 7:
        return "0111"
    elif num == 8:
        return "1000"
    elif num == 9:
        return "1001"
    elif num == 10:
        return "1010"
    elif num == 11:
        return "1011"
    elif num == 12:
        return "1100"
    elif num == 13:
        return "1101"
    elif num == 14:
        return "1110"
    elif num == 15:
        return "1111"
outString = []
for i in range(128):
    lengths = "hfdlxzhv-" + str(i)
    print lengths
    lengthsAscii = []
    for char in lengths:
        lengthsAscii.append(ord(char))
    for num in [17,31,73,47,23]:
        lengthsAscii.append(num)
    skipSize = 0
    currentPos = 0
    numbers = []
    for i in range(256):
        numbers.append(i)
    def increment(currentPos):
        if(currentPos == len(numbers) - 1):
            return 0
        else:
            return currentPos + 1
    def decrement(currentPos):
        if currentPos == 0:
            return len(numbers) - 1
        else:
            return currentPos - 1
    for i in range(64):
        for length in lengthsAscii:
            flipList = []
            lenCounter = length
            while lenCounter > 0:
                flipList.append(numbers[currentPos])
                currentPos = increment(currentPos)
                lenCounter -= 1
            flipList.reverse()
            lenCounter = length - 1
            while lenCounter >= 0:
                currentPos = decrement(currentPos)
                numbers[currentPos] = flipList[lenCounter]
                lenCounter -= 1
            for i in range(length):
                currentPos = increment(currentPos)
            for i in range(skipSize):
                currentPos = increment(currentPos)
            skipSize += 1
    counter = 0
    denseHash = []
    for i in range(len(numbers)/16):
        result = 0
        for i in range(16):
            result ^= numbers[counter + i]
        denseHash.append(result)
        counter += 16
    hexString = ""
    for num in denseHash:
        hexString += toBinary(int(num/16))
        hexString += toBinary(num%16)
    outString.append(hexString)
print outString
touched = []
def contiguous(i, j):
    global outString
    global touched
    if i < 0 or j < 0 or i > 127 or j > 127 or touched.count([i,j]) > 0:
        print "Failing at i=" + str(i) + ", j=" + str(j)
        return False
    if outString[i][j] == "1":
        touched.append([i,j])
        print "recursing at i=" + str(i) + ", j=" + str(j)
        contiguous(i-1,j)
        contiguous(i+1,j)
        contiguous(i,j-1)
        contiguous(i,j+1)
        return True
    return False
groupCount = 0
for i in range(128):
    for j in range(128):
        if contiguous(i,j):
            groupCount += 1
print groupCount