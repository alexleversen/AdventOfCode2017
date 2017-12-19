stepCount = 369
ls = [0]
currentPos = 0
def next():
    global ls
    global currentPos
    if currentPos == len(ls) - 1:
        currentPos = 0
    else:
        currentPos += 1
i = 1
while i <= 50000000:
    if i % 1000 == 0:
        print i
    for j in range(stepCount + 1):
        next()
    ls.insert(currentPos, i)
    i += 1
print ls[ls.index(0) + 1]