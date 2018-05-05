import random

def character():    #creates a character
    global strength
    global dex
    global con
    global con
    global intel
    global wis
    global cha
    global hp
    global hpMax
    global ac
    global gp
    global inventory
    global charClass

    print("Intro")

    x = 0
    while x == 0:
        try:
            print("Select Character")
            print("1: cleric")
            print("2: fighter")
            print("3: rogue")
            print("4: wizard")
            charChoice = int(input(""))

            if charChoice == 1:                 #cleric
                strength = random.randint(1,5)
                dex = random.randint(-5,-1)
                con = random.randint(-5,-1)
                intel = random.randint(-5,-1)
                wis = random.randint(1,5)
                cha = random.randint(1,5)
                hp = random.randint(5,15)
                hpMax = hp
                ac = 12
                gp = random.randint(30,50)
                inventory = ['studded leather','shortsword']
                charClass = 'Cleric'

            if charChoice == 2:                 #fighter
                strength = random.randint(1,5)
                dex = random.randint(1,5)
                con = random.randint(1,5)
                intel = random.randint(-5,-1)
                wis = random.randint(-5,-1)
                cha = random.randint(-5,-1)
                hp = random.randint(10,20)
                hpMax = hp
                ac = 14
                gp = random.randint(20,40)
                inventory = ['scalemail','longsword']
                charClass = 'Fighter'


            if charChoice == 3:                 #rogue
                strength = random.randint(-5,-1)
                dex = random.randint(1,5)
                con = random.randint(-5,-1)
                intel = random.randint(1,5)
                wis = random.randint(-5,-1)
                cha = random.randint(1,5)
                hp = random.randint(5,15)
                hpMax = hp
                ac = 11 + dex
                gp = random.randint(40,60)
                inventory = ['leather armor','dagger',]
                charClass = 'Rogue'


            if charChoice == 4:                 #wizard
                strength = random.randint(-5,-1)
                dex = random.randint(-5,-1)
                con = random.randint(-5,-1)
                intel = random.randint(1,5)
                wis = random.randint(1,5)
                cha = random.randint(1,5)
                hp = random.randint(5,10)
                hpMax = hp
                ac = 10 + dex
                gp = 55 + intel
                inventory = ['none','staff']
                charClass = 'Wizard'
            x = 1
        except:
            'try again'
            print("\nThat\'s not an acceptable input\n")

    summary()


def summary():
    global strength
    global dex
    global con
    global con
    global intel
    global wis
    global cha
    global hp
    global hpMax
    global ac
    global gp
    global inventory
    global charClass

    x = 'n'
    while x != 'y':
        try:
            print("Your Character:\n"),
            print("Class:",charClass)
            print("str:",strength)
            print("dex:",dex)
            print("con:",con)
            print("int:",intel)
            print("wis:",wis)
            print("cha:",cha)
            print("hp:",hp)
            print("ac:",ac)
            print("gp:",gp)
            print("Your inventory:",inventory)
            x = input("\ncontinue? (y/n)")
        except:
            'try again'

character()