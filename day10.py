lengths = "Hello there, my name is Alex Leversen"
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
def toHexString(num):
    if num < 10:
        return str(num)
    elif num == 10:
        return "a"
    elif num == 11:
        return "b"
    elif num == 12:
        return "c"
    elif num == 13:
        return "d"
    elif num == 14:
        return "e"
    elif num == 15:
        return "f"
hexString = ""
for num in denseHash:
    hexString += toHexString(int(num/16))
    hexString += toHexString(num%16)
print hexString
