import random as r

numRolls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0, 1000000):
    d = [0,0,0,0]

    d[0] = r.randint(1,6)
    d[1] = r.randint(1,6)
    d[2] = r.randint(1,6)
    d[3] = r.randint(1,6)


    d.sort()
    d.pop(0)

    x = sum(d) - 3
    numRolls[x] = numRolls[x] + 1

print(numRolls)
print("")
for i in range(0,16):
    x = round(numRolls[i] / sum(numRolls),3)
    val = i + 3
    print(val, ":",x)
print("")

for i in range(0,16):
    x = round((numRolls[i] / numRolls[0]))
    val = i + 3
    print(val, ":",x)