import random
program = "set i 31\nset a 1\nmul p 17\njgz p p\nmul a 2\nadd i -1\njgz i -2\nadd a -1\nset i 127\nset p 952\nmul p 8505\nmod p a\nmul p 129749\nadd p 12345\nmod p a\nset b p\nmod b 10000\nsnd b\nadd i -1\njgz i -9\njgz a 3\nrcv b\njgz b -1\nset f 0\nset i 126\nrcv a\nrcv b\nset p a\nmul p -1\nadd p b\njgz p 4\nsnd a\nset a b\njgz 1 3\nsnd b\nset f 1\nadd i -1\njgz i -11\nsnd a\njgz f -16\njgz a -19".split("\n")
i = 0
j = 0
registers0 = [0]
regNames0 = ["p"]
registers1 = [1]
regNames1 = ["p"]
queue0 = []
queue1 = []
sendCount = 0
receiving0 = False
receiving1 = False
finished0 = False
finished1 = False
numSteps = 0
def isNumber(n):
    if n.isdigit():
        return True
    if n != None and len(n) > 1:
        return n[1:].isdigit() and n[0] == "-"
    return False
def getValue0(arg):
    if isNumber(arg):
        return int(arg)
    return registers0[regNames0.index(arg)]
def getValue1(arg):
    if isNumber(arg):
        return int(arg)
    return registers1[regNames1.index(arg)]
while(True):
    numSteps += 1
    if (receiving0 and receiving1) or (receiving0 and finished1) or (receiving1 and finished0):
        break
    if random.randint(1,100) % 2 == 0:
        instruction0 = program[i].split(" ")
        print "Program 0: "+program[i]
        cmd = instruction0[0]
        if not isNumber(instruction0[1]) and regNames0.count(instruction0[1]) == 0:
            regNames0.append(instruction0[1])
            registers0.append(0)
        if len(instruction0) == 3 and not isNumber(instruction0[2]) and regNames0.count(instruction0[2]) == 0:
            regNames0.append(instruction0[2])
            registers0.append(0)
        if cmd == "snd":
            queue1.append(getValue0(instruction0[1]))
        elif cmd == "set":
                registers0[regNames0.index(instruction0[1])] = getValue0(instruction0[2])
        elif cmd == "add":
            registers0[regNames0.index(instruction0[1])] = registers0[regNames0.index(instruction0[1])] + getValue0(instruction0[2])
        elif cmd == "mul":
            registers0[regNames0.index(instruction0[1])] = registers0[regNames0.index(instruction0[1])] * getValue0(instruction0[2])
        elif cmd == "mod":
            registers0[regNames0.index(instruction0[1])] = registers0[regNames0.index(instruction0[1])] % getValue0(instruction0[2])
        elif cmd == "rcv":
            if len(queue0) > 0:
                registers0[regNames0.index(instruction0[1])] = queue0[0]
                queue0.remove(queue0[0])
                receiving0 = False
            else:
                receiving0 = True
                i -= 1
        elif cmd == "jgz":
            if getValue0(instruction0[1]) > 0:
                i += (getValue0(instruction0[2]) - 1)
        i += 1
        if i < 0 or i >= len(program):
            finished0 = True
            break
        print queue0
    if random.randint(1,100) % 2 == 0:
        instruction1 = program[j].split(" ")
        print "Program 1: "+program[j]
        cmd = instruction1[0]
        if not isNumber(instruction1[1]) and regNames1.count(instruction1[1]) == 0:
            regNames1.append(instruction1[1])
            registers1.append(0)
        if len(instruction1) == 3 and not isNumber(instruction1[2]) and regNames1.count(instruction1[2]) == 0:
            regNames1.append(instruction1[2])
            registers1.append(0)
        if cmd == "snd":
            queue0.append(getValue1(instruction1[1]))
            sendCount += 1
        elif cmd == "set":
                registers1[regNames1.index(instruction1[1])] = getValue1(instruction1[2])
        elif cmd == "add":
            registers1[regNames1.index(instruction1[1])] = registers1[regNames1.index(instruction1[1])] + getValue1(instruction1[2])
        elif cmd == "mul":
            registers1[regNames1.index(instruction1[1])] = registers1[regNames1.index(instruction1[1])] * getValue1(instruction1[2])
        elif cmd == "mod":
            registers1[regNames1.index(instruction1[1])] = registers1[regNames1.index(instruction1[1])] % getValue1(instruction1[2])
        elif cmd == "rcv":
            if len(queue1) > 0:
                registers1[regNames1.index(instruction1[1])] = queue1[0]
                queue1.remove(queue1[0])
                receiving1 = False
            else:
                receiving1 = True
                j -= 1
        elif cmd == "jgz":
            if getValue1(instruction1[1]) > 0:
                j += (getValue1(instruction1[2]) - 1)
        j += 1
        if j < 0 or j >= len(program):
            finished1 = True
            break
        print queue1
print sendCount
