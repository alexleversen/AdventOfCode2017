virusMap = "#.....##.####.#.#########\n.###..#..#..####.##....#.\n..#########...###...####.\n.##.#.##..#.#..#.#....###\n...##....###..#.#..#.###.\n###..#...######.####.#.#.\n#..###..###..###.###.##..\n.#.#.###.#.#...####..#...\n##........##.####..##...#\n.#.##..#.#....##.##.##..#\n###......#..##.####.###.#\n....#..###..#######.#...#\n#####.....#.##.#..#..####\n.#.###.#.###..##.#..####.\n..#..##.###...#######....\n.#.##.#.#.#.#...###.#.#..\n##.###.#.#.###.#......#..\n###..##.#...#....#..####.\n.#.#.....#..#....##..#..#\n#####.#.##..#...##..#....\n##..#.#.#.####.#.##...##.\n..#..#.#.####...#........\n###.###.##.#..#.##.....#.\n.##..##.##...#..#..#.#..#\n#...####.#.##...#..#.#.##".split("\n")
newVirusMap = []
for i in range(len(virusMap)):
    newVirusMap.append([])
    for j in range(len(virusMap)):
        newVirusMap[i].append(virusMap[i][j])
virusMap = newVirusMap
x = int(len(virusMap)/2)
y = x
counter = 0
infectedCount = 0
direction = "up"
def turnLeft():
    global direction
    if direction == "up":
        direction = "left"
    elif direction == "left":
        direction = "down"
    elif direction == "down":
        direction = "right"
    else:
        direction = "up"
def turnRight():
    global direction
    if direction == "up":
        direction = "right"
    elif direction == "right":
        direction = "down"
    elif direction == "down":
        direction = "left"
    else:
        direction = "up"
def move():
    global x
    global y
    if direction == "up":
        y -= 1
        if y < 0:
            y += 1
            virusMap.insert(0,[])
            for i in range(len(virusMap[1])):
                virusMap[0].append(".")
    elif direction == "right":
        x += 1
        if x >= len(virusMap[0]):
            for i in range(len(virusMap)):
                virusMap[i].append(".")
    elif direction == "down":
        y += 1
        if y == len(virusMap):
            virusMap.append([])
            for i in range(len(virusMap[0])):
                virusMap[len(virusMap)-1].append(".")
    elif direction == "left":
        x -= 1
        if x < 0:
            x += 1
            for i in range(len(virusMap)):
                virusMap[i].insert(0,".")
while counter < 10000:
    print y
    print x
    print counter
    currentNode = virusMap[y][x]
    if currentNode == ".":
        turnLeft()
        virusMap[y][x] = "#"
        infectedCount += 1
        move()
    else:
        turnRight()
        virusMap[y][x] = "."
        move()
    counter += 1
print virusMap
print infectedCount
