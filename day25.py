state = "A"
tape = [0]
currentSlot = 0
checkSumSteps = 12317297
def moveRight():
    global currentSlot
    currentSlot += 1
    if currentSlot == len(tape):
        tape.append(0)
def moveLeft():
    global currentSlot
    currentSlot -= 1
    if currentSlot < 0:
        tape.insert(0, 0)
        currentSlot += 1
def nextState(num):
    global state
    if state == "A":
        if num == 0:
            tape[currentSlot] = 1
            moveRight()
            state = "B"
        else:
            tape[currentSlot] = 0
            moveLeft()
            state = "D"
    elif state == "B":
        if num == 0:
            tape[currentSlot] = 1
            moveRight()
            state = "C"
        else:
            tape[currentSlot] = 0
            moveRight()
            state = "F"
    elif state == "C":
        if num == 0:
            tape[currentSlot] = 1
            moveLeft()
            state = "C"
        else:
            tape[currentSlot] = 1
            moveLeft()
            state = "A"
    elif state == "D":
        if num == 0:
            tape[currentSlot] = 0
            moveLeft()
            state = "E"
        else:
            tape[currentSlot] = 0
            moveRight()
            state = "A"
    elif state == "E":
        if num == 0:
            tape[currentSlot] = 1
            moveLeft()
            state = "A"
        else:
            tape[currentSlot] = 0
            moveRight()
            state = "B"
    elif state == "F":
        if num == 0:
            tape[currentSlot] = 0
            moveRight()
            state = "C"
        else:
            tape[currentSlot] = 0
            moveRight()
            state = "E"
i = 0
while i < checkSumSteps:
    if i % 100000 == 0:
        print i
    nextState(tape[currentSlot])
    i += 1
count = 0
for n in range(len(tape)):
    print n
    if tape[n] == 1:
        count += 1
print count