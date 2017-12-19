import copy
class Firewall:
    def __init__(self, size):
        self.size = size
        self.index = 0
        self.direction = 1
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "[Index: " + str(self.index) + ", Size: " + str(self.size) + ", Direction: " + str(self.direction) + "]"
    def move(self):
        if self.index == 0 and self.direction == 0:
            self.direction = 1
            if self.size > 1:
                self.index = 1
        elif self.index == self.size - 1 and self.direction == 1:
            self.direction = 0
            self.index -= 1
        else:
            if self.direction == 1:
                self.index += 1
            elif self.direction == 0:
                self.index -= 1
nums = "0:3\n1:2\n2:5\n4:4\n6:4\n8:6\n10:6\n12:6\n14:8\n16:6\n18:8\n20:8\n22:8\n24:12\n26:8\n28:12\n30:8\n32:12\n34:12\n36:14\n38:10\n40:12\n42:14\n44:10\n46:14\n48:12\n50:14\n52:12\n54:9\n56:14\n58:12\n60:12\n64:14\n66:12\n70:14\n76:20\n78:17\n80:14\n84:14\n86:14\n88:18\n90:20\n92:14\n98:18".split("\n")
lastIndex = int(nums[len(nums)-1].split(":")[0])
delay = 0
ind = 0
startState = []
for i in range(lastIndex + 1):
    if int(nums[ind].split(":")[0]) == i:
        startState.append(Firewall(int(nums[ind].split(":")[1])))
        ind += 1
    else:
        startState.append(None)

while True:
    firewalls = copy.deepcopy(startState)
    severity = 0
    caught = False
    for i in range(len(firewalls)):
        if firewalls[i] != None:
            if firewalls[i].index == 0:
                severity += (i * firewalls[i].size)
                if i == 0:
                    caught = True
        for j in range(len(firewalls)):
            if firewalls[j] != None:
                firewalls[j].move()
    if severity == 0 and not caught:
        break
    if delay % 1000 == 0:
        print "."
    delay += 1
    for wall in startState:
        if wall != None:
            wall.move()
print delay
