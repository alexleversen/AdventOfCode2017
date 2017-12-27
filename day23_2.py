startValue = 106500
endValue = 106500 + 17000
increment = 17
outputValue = 0
while(startValue <= endValue):
    for i in range(2, startValue):
        if startValue % i == 0:
            outputValue += 1
            break
    startValue += increment
print outputValue