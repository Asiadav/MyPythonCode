import random

numList = []
x = 0
while x != 5:
    num = random.randrange(1,70)
    if num in numList:
        'do nothing'
    else:
        numList.append(num)
        x += 1
numList.sort()
pb = random.randrange(1,27)

print("The numbers are:")
for i in range(0,5):
    print(numList[i])

print("...and the powerball is:")
print(pb,"!")