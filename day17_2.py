stepCount = 369
listLength = 1
index = listLength - 1
def next():
    global stepCount
    global index
    global listLength
    if index + stepCount + 1 > listLength:
        if listLength <= stepCount:
            if listLength == 1:
                index = 1
            else:
                index += ((stepCount % listLength) + 1)
                if index > listLength:
                    index -= (listLength)
        else:
            index = stepCount - (listLength - 1 - index)
    else:
        index += (stepCount + 1)
lastValAtIndex = -1
while listLength <= 50000000:
    if index == 1:
        lastValAtIndex = listLength - 1
    if listLength % 10000 == 0:
        print listLength
        print index
    next()
    listLength += 1
print lastValAtIndex