a = 1
b = 6
c = 6
d = 0
e = 0
f = 0
g = 0
h = 0
c += 1
while(True):
    f = 1
    d = 2
    while True:
        e = 2
        while True:
            g = d * e - b
            if g == 0:
                f = 0
            e += 1
            g = e - b
            if g == 0:
                break
        d += 1
        g = d - b
        if g == 0:
            break
    if f == 0:
        h += 1
    g = b - c
    if g == 0:
        break
    b += 1
print h