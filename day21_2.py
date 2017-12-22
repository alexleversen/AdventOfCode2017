import copy
rulesFullText = "../..=>.../.../###\n#./..=>.../.#./.##\n##/..=>.#./.#./...\n.#/#.=>###/..#/.##\n##/#.=>..#/###/#..\n##/##=>..#/#../##.\n.../.../...=>.##./##../..##/.##.\n#../.../...=>##../.#.#/..#./###.\n.#./.../...=>##.#/#.#./.#../..##\n##./.../...=>...#/##.#/.#.#/#.##\n#.#/.../...=>..#./#.../###./...#\n###/.../...=>#.#./...#/#.#./###.\n.#./#../...=>...#/###./.##./...#\n##./#../...=>###./####/###./..##\n..#/#../...=>####/#.../####/#.##\n#.#/#../...=>#.##/.#.#/##.#/###.\n.##/#../...=>..../.#../.#.#/.##.\n###/#../...=>..##/##.#/..##/.###\n.../.#./...=>###./..##/.#../#..#\n#../.#./...=>###./.#../#.../#...\n.#./.#./...=>####/..#./.##./##..\n##./.#./...=>.#../#.#./###./###.\n#.#/.#./...=>####/.##./##.#/.###\n###/.#./...=>#.#./..##/.##./#...\n.#./##./...=>####/#.##/####/..#.\n##./##./...=>#.../.#../..../#.##\n..#/##./...=>#..#/..##/#.../####\n#.#/##./...=>###./##../..##/#...\n.##/##./...=>..../#.##/.###/#.#.\n###/##./...=>.#../##.#/.#../##..\n.../#.#/...=>...#/.###/.##./###.\n#../#.#/...=>###./##../#.#./.##.\n.#./#.#/...=>..#./.#../.##./.###\n##./#.#/...=>#.../#.../.##./.#..\n#.#/#.#/...=>.##./..##/.###/#...\n###/#.#/...=>..../####/###./....\n.../###/...=>#.##/.#.#/#.##/...#\n#../###/...=>#.../#.#./.#../#...\n.#./###/...=>...#/###./.##./.#.#\n##./###/...=>##../####/###./#.##\n#.#/###/...=>...#/###./##.#/.#.#\n###/###/...=>#.#./##.#/..../.##.\n..#/.../#..=>...#/..#./..#./##..\n#.#/.../#..=>..#./#.##/#.#./#.##\n.##/.../#..=>####/####/#.##/#...\n###/.../#..=>###./..#./###./.#..\n.##/#../#..=>...#/####/..../###.\n###/#../#..=>##.#/.#../##.#/...#\n..#/.#./#..=>###./#.##/...#/##..\n#.#/.#./#..=>#.../..#./..#./#.##\n.##/.#./#..=>##.#/...#/#.#./.###\n###/.#./#..=>.#../..##/#.#./..#.\n.##/##./#..=>#.../#.#./.###/#...\n###/##./#..=>.##./.#../.#.#/.###\n#../..#/#..=>###./#..#/#.../##.#\n.#./..#/#..=>#.#./#..#/#.../.###\n##./..#/#..=>...#/..##/..#./####\n#.#/..#/#..=>####/#..#/###./#.#.\n.##/..#/#..=>..#./..#./..../.##.\n###/..#/#..=>...#/#..#/#.#./....\n#../#.#/#..=>..##/.#.#/.###/.##.\n.#./#.#/#..=>..../##.#/..##/#..#\n##./#.#/#..=>..#./..##/#..#/#..#\n..#/#.#/#..=>..#./#.../#.#./##..\n#.#/#.#/#..=>##.#/..##/.###/...#\n.##/#.#/#..=>#.##/.##./##../#.#.\n###/#.#/#..=>####/##.#/#..#/#.#.\n#../.##/#..=>..##/#.#./####/####\n.#./.##/#..=>##../###./####/....\n##./.##/#..=>.###/####/..#./...#\n#.#/.##/#..=>###./##../##../#.##\n.##/.##/#..=>##../.###/####/.#.#\n###/.##/#..=>##../.##./#.../..#.\n#../###/#..=>#.#./.#.#/#.../....\n.#./###/#..=>.##./##../...#/##..\n##./###/#..=>#.#./..../.##./##.#\n..#/###/#..=>...#/...#/##.#/...#\n#.#/###/#..=>.##./.###/#..#/.##.\n.##/###/#..=>####/..##/#.../####\n###/###/#..=>...#/####/..#./.###\n.#./#.#/.#.=>.##./#.##/.##./.###\n##./#.#/.#.=>..##/.#../##.#/###.\n#.#/#.#/.#.=>.#../..../.#.#/#...\n###/#.#/.#.=>###./..#./..../#.#.\n.#./###/.#.=>#..#/.#../#.../..##\n##./###/.#.=>.##./...#/.###/....\n#.#/###/.#.=>.###/###./#.#./.#.#\n###/###/.#.=>#.##/.#.#/#.#./.##.\n#.#/..#/##.=>.###/..../####/####\n###/..#/##.=>#.##/###./..##/.##.\n.##/#.#/##.=>..../...#/#..#/..##\n###/#.#/##.=>#.##/.#../.#../....\n#.#/.##/##.=>..##/..##/#.../#..#\n###/.##/##.=>##.#/#.../#.##/..##\n.##/###/##.=>...#/..#./##../#.##\n###/###/##.=>#.##/#..#/..#./...#\n#.#/.../#.#=>##.#/.#../##.#/.##.\n###/.../#.#=>#.#./..##/.#.#/##.#\n###/#../#.#=>..#./#.##/...#/.###\n#.#/.#./#.#=>.###/#.##/#..#/#.##\n###/.#./#.#=>..../..#./###./..#.\n###/##./#.#=>.###/##../..##/####\n#.#/#.#/#.#=>#.#./####/.#../.##.\n###/#.#/#.#=>####/..../..##/#...\n#.#/###/#.#=>#.../.##./#.../...#\n###/###/#.#=>.#.#/...#/..../..##\n###/#.#/###=>.#../#.##/#.##/.###\n###/###/###=>#.../.#.#/#..#/#.##".split("\n")
def rotate(array):
    newArray = []
    for i in range(len(array)):
        newArray.append([])
        for j in range(len(array)):
            newArray[i].append(array[len(array) - j - 1][i])
    return newArray
def flipH(array):
    for row in array:
        row.reverse()
def flipV(array):
    array.reverse()
class Rule:
    def __init__(self, ruleText):
        kvp = ruleText.split("=>")
        key = kvp[0].split("/")
        val = kvp[1].split("/")
        self.keyArray = []
        for row in key:
            rowArray = []
            for c in row:
                if c == ".":
                    rowArray.append(False)
                else:
                    rowArray.append(True)
            self.keyArray.append(rowArray)
        self.valArray = []
        for row in val:
            rowArray = []
            for c in row:
                if c == ".":
                    rowArray.append(False)
                else:
                    rowArray.append(True)
            self.valArray.append(rowArray)
    def match(self,chunk):
        if len(chunk) != len(self.keyArray):
            return None
        arrayCopy = copy.deepcopy(chunk)
        for i in range(4):
            if arrayCopy == self.keyArray:
                ruleOut = copy.deepcopy(self.valArray)
                return ruleOut
            flipH(arrayCopy)
            if arrayCopy == self.keyArray:
                ruleOut = copy.deepcopy(self.valArray)
                return ruleOut
            flipH(arrayCopy)
            flipV(arrayCopy)
            if arrayCopy == self.keyArray:
                ruleOut = copy.deepcopy(self.valArray)
                return ruleOut
            flipV(arrayCopy)
            arrayCopy = rotate(arrayCopy)
        return None
rules = []
for rule in rulesFullText:
    rules.append(Rule(rule))
startArray = [[False,True,False],[False,False,True],[True,True,True]]
def iterate(array, rules):
    i = 0
    newArray = []
    if len(array) % 2 == 0:
        rng = len(array) + len(array)/2
        for x in range(rng):
            newArray.append([])
        while i < len(array):
            j = 0
            while j < len(array):
                currentChunk = [[array[i][j],array[i][j+1]],[array[i+1][j],array[i+1][j+1]]]
                for rule in rules:
                    ruleOut = rule.match(currentChunk)
                    if ruleOut != None:
                        for k in range(3):
                            for l in range(3):
                                newArray[i + i/2 + k].append(ruleOut[k][l])
                j += 2
            i += 2
    else:
        rng = len(array) + len(array)/3
        for x in range(rng):
            newArray.append([])
        while i < len(array):
            j = 0
            while j < len(array):
                currentChunk = [[array[i][j],array[i][j+1],array[i][j+2]],[array[i+1][j],array[i+1][j+1],array[i+1][j+2]],[array[i+2][j],array[i+2][j+1],array[i+2][j+2]]]
                for rule in rules:
                    ruleOut = rule.match(currentChunk)
                    if ruleOut != None:
                        for k in range(4):
                            for l in range(4):
                                newArray[i + i/3 + k].append(ruleOut[k][l])
                j += 3
            i += 3
    return newArray
print startArray
for i in range(18):
    startArray = iterate(startArray, rules)
    print startArray
    print i
truthCount = 0
for i in range(len(startArray)):
    for j in range(len(startArray)):
        if startArray[i][j]:
            truthCount += 1
print truthCount