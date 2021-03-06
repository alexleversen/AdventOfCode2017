import copy
partsString = "14/42\n2/3\n6/44\n4/10\n23/49\n35/39\n46/46\n5/29\n13/20\n33/9\n24/50\n0/30\n9/10\n41/44\n35/50\n44/50\n5/11\n21/24\n7/39\n46/31\n38/38\n22/26\n8/9\n16/4\n23/39\n26/5\n40/40\n29/29\n5/20\n3/32\n42/11\n16/14\n27/49\n36/20\n18/39\n49/41\n16/6\n24/46\n44/48\n36/4\n6/6\n13/6\n42/12\n29/41\n39/39\n9/3\n30/2\n25/20\n15/6\n15/23\n28/40\n8/7\n26/23\n48/10\n28/28\n2/13\n48/14".split("\n")
parts = []
for part in partsString:
    partStrs = part.split("/")
    part1 = int(partStrs[0])
    part2 = int(partStrs[1])
    parts.append([part1,part2])
def bridgeLen(length, remainingParts, pin):
    foundPart = False
    possibleParts = []
    for part in remainingParts:
        if part[0] == pin:
            foundPart = True
            possibleParts.append(bridgeLen(length + 1, [p for p in remainingParts if p != part], part[1]))
        elif part[1] == pin:
            foundPart = True
            possibleParts.append(bridgeLen(length + 1, [p for p in remainingParts if p != part], part[0]))
    if foundPart:
        maxLen = -1
        for part in possibleParts:
            if part > maxLen:
                maxLen = part
        return 1 + maxLen
    return 1
maxLengths = []
for part in parts:
    if part[0] == 0:
        maxLengths.append(bridgeLen(1, [p for p in parts if p != part], part[1]))
    elif part[1] == 0:
        maxLengths.append(bridgeLen(1, [p for p in parts if p != part], part[0]))
maxLength = -1
for length in maxLengths:
    if length > maxLength:
        maxLength = length
def maxStrengthAtLength(length, strength, remainingParts, pin):
    global maxLength
    if length == maxLength:
        return strength
    remPartsStrengths = []
    for part in remainingParts:
        if part[0] == pin:
            remPartsStrengths.append(maxStrengthAtLength(length + 1, strength + part[0] + part[1], [p for p in remainingParts if p != part], part[1]))
        elif part[1] == pin:
            remPartsStrengths.append(maxStrengthAtLength(length + 1, strength + part[0] + part[1], [p for p in remainingParts if p != part], part[0]))
    maxStrength = -1
    for strength in remPartsStrengths:
        if strength > maxStrength:
            maxStrength = strength
    return maxStrength
maxStrengths = []
for part in parts:
    if part[0] == 0:
        maxStrengths.append(maxStrengthAtLength(1, part[0] + part[1], [p for p in parts if p != part], part[1]))
    elif part[1] == 0:
        maxStrengths.append(maxStrengthAtLength(1, part[0] + part[1], [p for p in parts if p != part], part[0]))
maxStrength = -1
for strength in maxStrengths:
    if strength > maxStrength:
        maxStrength = strength
print maxStrength