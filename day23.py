program = "set b 65\nset c b\njnz a 2\njnz 1 5\nmul b 100\nsub b -100000\nset c b\nsub c -17000\nset f 1\nset d 2\nset e 2\nset g d\nmul g e\nsub g b\njnz g 2\nset f 0\nsub e -1\nset g e\nsub g b\njnz g -8\nsub d -1\nset g d\nsub g b\njnz g -13\njnz f 2\nsub h -1\nset g b\nsub g c\njnz g 2\njnz 1 3\nsub b -17\njnz 1 -23".split("\n")
registers = [0,0,0,0,0,0,0,0]
registerNames = ["a","b","c","d","e","f","g","h"]
index = 0
mulCount = 0
def isNumber(n):
    if n.isdigit():
        return True
    if n != None and len(n) > 1:
        return n[1:].isdigit() and n[0] == "-"
    return False
def getValue(value):
    if isNumber(value):
        return int(value)
    else:
        return registers[registerNames.index(value)]
def execute(instruction):
    global index
    global mulCount
    arg0 = instruction[1]
    arg1 = instruction[2]
    instr = instruction[0]
    if instr == "set":
        registers[registerNames.index(arg0)] = getValue(arg1)
    elif instr == "sub":
        registers[registerNames.index(arg0)] -= getValue(arg1)
    elif instr == "mul":
        registers[registerNames.index(arg0)] *= getValue(arg1)
        mulCount += 1
    else: #"jnz"
        if getValue(arg0) != 0:
            index += (getValue(arg1) - 1)
    index += 1
while(index >= 0 and index < len(program)):
    execute(program[index].split(" "))
print mulCount

