banks = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]
initialState = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]
cycleCount = 0
while True:
    index = -1
    maxNum = -1
    for i in range(len(banks)):
        if(banks[i] > maxNum):
            maxNum = banks[i]
            index = i
    banks[index] = 0
    while maxNum > 0:
        index = index + 1
        if index == len(banks):
            index = 0
        banks[index] = banks[index] + 1
        maxNum = maxNum - 1
    cycleCount += 1
    if banks == initialState:
        break
print cycleCount
