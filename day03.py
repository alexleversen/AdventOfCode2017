from itertools import repeat
import pprint
pp = pprint.PrettyPrinter()
num = 325489
array = []
for i in range(10):
    array.append(list(repeat(0,10)))
x = 5
y = 5
state = 1
counter = 1
array[x][y] = 1

def nextDirection():
    if state == 3:
        return 0
    return state + 1
def updateSum():
    array[x][y] = array[x-1][y-1] + array[x-1][y] + array[x-1][y+1] + array[x][y-1] + array[x][y+1] + array[x+1][y-1] + array[x+1][y] + array[x+1][y+1]
    pp.pprint(array)
    if array[x][y] > num:
        pp.pprint(array[x][y])
        exit()
while True:
    if state == 0:
        for i in range(counter):
            x += 1
            updateSum()
    elif state == 1:
        for i in range(counter):
            y -= 1
            updateSum()
    elif state == 2:
        for i in range(counter):
            x -= 1
            updateSum()
    else:
        for i in range(counter):
            y += 1
            updateSum()
    state = nextDirection()
    if state == 0:
        for i in range(counter):
            x += 1
            updateSum()
    elif state == 1:
        for i in range(counter):
            y -= 1
            updateSum()
    elif state == 2:
        for i in range(counter):
            x -= 1
            updateSum()
    else:
        for i in range(counter):
            y += 1
            updateSum()
    state = nextDirection()
    counter += 1
