import random

def makeStats(statList):                #makes 6 dnd stats
    valueList = [0,0,0,0,0,0]
    v = sum(valueList)
    s = sum(statList)
    attempts = 0
    while sum(valueList) <= sum(statList):

        for statNum in range(0,6):       #makes 6 stat values
            x = [0,0,0,0]
            for i in range(3):
                x[i] = random.randint(1,6)
            x.sort()
            x.pop(0)
            val = sum(x)
            valueList[statNum] = val      #sets value as a stat

        attempts += 1
        #print(valueList)
        if attempts % 100000 == 0:
            print("attempting...",attempts)
        if attempts == 1000000:
            print("Too hard!\n")
            break
    if attempts == 1000000:
        print("You will never achieve this value")
    else:
        print("\nYour stats are: ")
        print(valueList)                  #prints out best/winning stat list

    return attempts

def howLong():                          #takes user input of stats and outputs attempts
    userList = [0,0,0,0,0,0]
    counter = 0
    print("let\'s attempt making DnD stats!")
    while counter != 6:                 #takes user input and ensures success
        success = 1
        try:
            reqStats = int(input("\nGive Desired Stat "))
        except:
            print("A number, stupid. Insert a number.")
            success = 0
        if success == 1:
            if reqStats > 2 and reqStats < 19:
                userList[counter] = reqStats
                counter += 1
            else:
                print("That's not possible stat value")

    x = makeStats(userList)             #makes the stats and x is attepts
    if x != 1000000:
        print("That will take",x,"attempts")

howLong()