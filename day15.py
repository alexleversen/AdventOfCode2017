genAValue = 873
genBValue = 583
multiplierA = 16807
multiplierB = 48271
divider = 2147483647
bitmask = 65535
count = 0
genAList = []
genBList = []
i = 0
while(min(len(genAList),len(genBList)) <= 5000000):
    if i % 100000 == 0:
        print i
    genAValue = (genAValue * multiplierA) % divider
    genBValue = (genBValue * multiplierB) % divider
    if genAValue % 4 == 0:
        genAList.append(genAValue)
    if genBValue % 8 == 0:
        genBList.append(genBValue)
    i += 1
for i in range(min(len(genAList),len(genBList))):
    if (genAList[i] & bitmask) == (genBList[i] & bitmask):
        count += 1
print count