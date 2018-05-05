import random
import easygui
import time
global strength
strength = 0
global dex
dex = 0
global con
con = 0
global intel
intel = 0
global wis
wis = 0
global cha
cha = 0

global food
food = 2
global hp
hp = 0
global hpMax
hpMax = 0
global ac
ac = 0
global gp
gp = 0

global charClass
charClass = 'none'
global inventory
inventory = []
global scalemail
global chainmail
scalemail = 0
chainmail = 0

global weapon1
global weapon2
weapon1 = 0
weapon2 = 0

global atkLo
global atkHi

atkLo = 0
atkHi = 0

global spellbook
spellbook = []

def character():    #creates a character
    global strength
    global dex
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
    global spellbook
    global atkLo
    global atkHi


    easygui.msgbox("\nWelcome to your journey traveler-guy!\nMake your character, buy your wares\nand head out on adventure!\n")

    x = 0
    while x == 0:
        try:
            charChoice = easygui.buttonbox("Select Character\n1: cleric\n2: fighter\n3: rogue\n4: wizard", '', ('1','2','3','4'))
            print(charChoice)

            if charChoice == '1':                 #cleric
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
                calcATK()
                charClass = 'Cleric'
                print(charClass)

            if charChoice == '2':                 #fighter
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
                calcATK()

                charClass = 'Fighter'


            if charChoice == '3':                 #rogue
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
                calcATK()

                charClass = 'Rogue'


            if charChoice == '4':                 #wizard
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
                inventory = ['no armor','fire bolt spell']
                calcATK()

                charClass = 'Wizard'
            if charChoice !='1' and charChoice !='2' and charChoice !='3'and charChoice !='4':
                heck + 1
            x = 1

        except:
            'try again'
            easygui.msgbox("\nThat\'s not an acceptable input\n")

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
    global spellbook
    global atkLo
    global atkHi
    x = 'n'
    while x != 'y':
        try:
            easygui.msgbox("Your Character:\nClass:"+charClass+"\nstr:"+str(strength))       ##broke
            easygui.msgbox("\ndex:",dex)
            easygui.msgbox("\ncon:",con)
            easygui.msgbox("\nint:",intel)
            easygui.msgbox("\nwis:",wis)
            easygui.msgbox("\ncha:",cha)
            easygui.msgbox("\nhp:",hp,"/",hpMax)
            easygui.msgbox("\nac:",ac)
            easygui.msgbox("\ngp:",gp)

            easygui.msgbox("Your inventory:",inventory)
            easygui.msgbox("weapon damage:",atkLo,"-",atkHi)

        except:
            'try again'


def town():
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
    global spellbook
    global atkLo
    global atkHi
    easygui.msgbox("\nWelcome to the town\nit\'s a bustling community of many cold and lifeless\npeople that don\'t like you, but at least\nthey will let you stay just long enough to\nbuy supplies and leave forever.\nRun along now.")
    time.sleep(8)
    x = 0
    while x == 0:
        try:
            easygui.msgbox("\nWhat will you do?")
            easygui.msgbox("1: Go to the shop")
            easygui.msgbox("2: View character summary")
            easygui.msgbox("3: Talk to people")
            easygui.msgbox("4: Head out on your quest")
            choice = int(input(""))
            if choice == 1:
                shop()
            if choice == 2:
                summary()
            if choice == 3:
                talk()
            if choice == 4:
                easygui.msgbox("\nYou head out on your adventure")
                x = 1

        except:
            'try again'
def shop():
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
    global spellbook
    global atkLo
    global atkHi
    easygui.msgbox("\nWelcome to the shop\nBuy something or get out of my sight!")

    x = 0
    while x == 0:
        try:
            easygui.msgbox("\nWhat will you do?")
            easygui.msgbox("1: Buy")
            easygui.msgbox("2: Leave")
            choice = int(input(""))

            if choice == 1:
                wares()
            if choice == 2:
                x = 1

        except:
            'try again'

def wares():
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
    global spellbook
    global atkLo
    global atkHi
    x = 0
    while x == 0:
        try:
            easygui.msgbox("\nHere is what I have:")
            easygui.msgbox("1: armor upgrade")
            easygui.msgbox("2: weapon upgrade")
            easygui.msgbox("3: health potion")
            easygui.msgbox("4: food")
            x = int(input(""))

            if x == 1:
                armorUp()
            if x == 2:
                weaponUp()
            if x == 3:
                easygui.msgbox("\nBuy a potion to increase maximum health for 10gp?")
                choice = input("y/n")
                if choice == 'y':
                    if gp >= 10:
                        gp = gp - 10
                        hp = hp + random.randint(4,7)
                        hpMax = hp
                    else:
                        easygui.msgbox("\nYou can\'t afford that")
                else:
                    'nah'
            if x == 4:
                easygui.msgbox("\nBuy food for 5gp?")
                choice = input("y/n")
                if choice == 'y':
                    if gp >= 5:
                        gp = gp - 5
                        food += 5
                    else:
                        easygui.msgbox("\nYou can\'t afford that")
                else:
                    'nah'
        except:
            'try again'

        calcATK()

def armorUp():
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
    global scalemail
    global chainmail
    global spellbook
    global atkLo
    global atkHi
    if charClass == 'Cleric':
        x = 0
        while x == 0:
            try:
                if scalemail == 0:
                    easygui.msgbox("1: Buy scalemail for 10gp")
                if chainmail == 0:
                    easygui.msgbox("2: Buy chainmail for 20gp")
                if chainmail == 1 and scalemail == 1:
                    easygui.msgbox("There is no more armor")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[0] = 'scalemail'
                        ac = 14
                        scalemail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[0] = 'chainmail'
                        ac = 16
                        chainmail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

            except:
                'try agian'


    if charClass == 'Fighter':
        x = 0
        while x == 0:
            try:
                if scalemail == 0:
                    easygui.msgbox("1: Buy chainmail for 10gp")
                if chainmail == 0:
                    easygui.msgbox("2: Buy plate armour for 20gp")
                if chainmail == 1 and scalemail == 1:
                    easygui.msgbox("There is no more armor")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[0] = 'chainmail'
                        ac = 16
                        scalemail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[0] = 'plate armor'
                        ac = 18
                        chainmail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

            except:
                'try agian'


    if charClass == 'Rogue':
        x = 0
        while x == 0:
            try:
                if scalemail == 0:
                    easygui.msgbox("1: Buy studded leather for 10gp")
                if chainmail == 0:
                    easygui.msgbox("2: Buy scalemail for 20gp")
                if chainmail == 1 and scalemail == 1:
                    easygui.msgbox("There is no more armor")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[0] = 'studded leather'
                        ac = 12 + dex
                        scalemail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[0] = 'scalemail'
                        ac = 14
                        if dex >= 1:
                            dex += 1
                        if dex >= 2:
                            dex += 1
                        chainmail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

            except:
                'try agian'


    if charClass == 'Wizard':
        x = 0
        while x == 0:
            try:
                if scalemail == 0:
                    easygui.msgbox("1: Buy leather armor for 10gp")
                if chainmail == 0:
                    easygui.msgbox("2: Buy mage armor for 20gp")
                if chainmail == 1 and scalemail == 1:
                    easygui.msgbox("There is no more armor")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[0] = 'leather armor'
                        ac = 11
                        scalemail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[0] = 'mage armor'
                        ac = 14 + dex
                        chainmail = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

            except:
                'try agian'

def weaponUp():
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
    global weapon1
    global weapon2
    global spellbook
    global atkLo
    global atkHi
    if charClass == 'Cleric':
        x = 0
        while x == 0:
            try:
                if weapon1 == 0:
                    easygui.msgbox("1: Buy longsword for 10gp")
                if weapon2 == 0:
                    easygui.msgbox("2: Buy lance for 20gp")
                if weapon1 == 1 and weapon2 == 1:
                    easygui.msgbox("There are no more weapons")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[1] = 'longsword'
                        weapon1 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[1] = 'lance'
                        weapon2 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

            except:
                'try agian'


    if charClass == 'Fighter':
        x = 0
        while x == 0:
            try:
                if weapon1 == 0:
                    easygui.msgbox("1: Buy lance for 10gp")
                if weapon2 == 0:
                    easygui.msgbox("2: Buy greatsword for 20gp")
                if weapon1 == 1 and weapon2 == 1:
                    easygui.msgbox("There are no more weapons")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[1] = 'lance'
                        weapon1 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[1] = 'greatsword'
                        weapon2 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")


            except:
                'try agian'


    if charClass == 'Rogue':
        x = 0
        while x == 0:
            try:
                if weapon1 == 0:
                    easygui.msgbox("1: Buy shortsword for 10gp")
                if weapon2 == 0:
                    easygui.msgbox("2: Buy rapier for 20gp")
                if weapon1 == 1 and weapon2 == 1:
                    easygui.msgbox("There are no more weapons")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[1] = 'shortsword'
                        weapon1 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[1] = 'rapier'
                        weapon2 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")


            except:
                'try agian'


    if charClass == 'Wizard':
        x = 0
        while x == 0:
            try:
                if weapon1 == 0:
                    easygui.msgbox("1: Buy magic missle spell for 10gp")
                if weapon2 == 0:
                    easygui.msgbox("2: Buy guiding bolt spell for 20gp")
                if weapon1 == 1 and weapon2 == 1:
                    easygui.msgbox("There are no more weapons")
                easygui.msgbox("3: Leave")
                x = int(input(""))

                if x == 1:
                    if gp >= 10:
                        gp = gp - 10
                        inventory[1] = 'magic missle spell'
                        weapon1 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")

                if x == 2:
                    if gp >= 20:
                        gp = gp - 20
                        inventory[1] = 'guiding bolt spell'
                        weapon2 = 1
                    else:
                        easygui.msgbox("You can\'t afford that")


            except:
                'try agian'

def calcATK():
    global atkLo
    global atkHi

    if inventory[1] == 'none':
        atkLo = 1
        atkHi = 2
    if inventory[1] == 'dagger':
        atkLo = 1 + dex
        atkHi = 4 + dex
    if inventory[1] == 'shortsword':
        atkLo = 1 + strength
        atkHi = 6 + strength
    if inventory[1] == 'rapier':
        atkLo = 1 + dex
        atkHi = 8 + dex
    if inventory[1] == 'longsword':
        atkLo = 1 + strength
        atkHi = 10 + strength
    if inventory[1] == 'greatsword':
        atkLo = 2 + strength
        atkHi = 12 + strength
    if inventory[1] == 'fire bolt spell':
        atkLo = 1
        atkHi = 10
    if inventory[1] == 'magic missle spell':
        atkLo = 6
        atkHi = 15
    if inventory[1] == 'guiding bolt spell':
        atkLo = 4
        atkHi = 24

def talk():
    x = random.randint(1,4)
    if x == 1:
        easygui.msgbox("\nYou're new to town and noone\nlikes or cares about you.\nYou do however find confidence\nin a tuft of grass")
        time.sleep(4)
    if x == 2:
        easygui.msgbox("You find a clump of dirt\nwith a charming personality")
        time.sleep(3)
    if x == 3:
        easygui.msgbox("You are physcially and emotionally alone")
        time.sleep(3)
    if x == 4:
        easygui.msgbox("Unable to find anyone in town that\nwill say anything but \'leave me alone\'\nyou decide to talk to yourself")
        time.sleep(4)
'''
def mooshroom():
    import random

    death = hp
    if hp <= 0:
        easygui.msgbox("You die")
        dead
    def feasygui.msgbox():
        h = input("Will you attack?\n:")
        if h == "Yes":
            enemy_HP - 1 = enemy_HP
            easygui.msgbox("You hit the enemy")

            if enemy_HP <= 0:
                easygui.msgbox("You die!")
        elif:





    x = random.randrange(1,11)
    if x == "1,6":
        r = input("You found a stream(1)\nWill you approach the stream?(2)\n:")
        if r == "1":
            easygui.msgbox("You approach the stream.")
            easygui.msgbox("You see a bear.")
            e = input("Will you fight, or flee?")
            if e == "Fight":
                feasygui.msgbox()
                while b = 3:
                    if b == 0:
                        easygui.msgbox("You die.")
                        dead
                    if b == 6:
                        easygui.msgbox("You win.")
        if r == "2":
            easygui.msgbox("You walk away from the stream.")
            easygui.msgbox("A wild mooshroom flys out of the bush beside you and starts to challenge you.")
            easygui.msgbox("Will you fight it?")
            if wis >= 2:
                easygui.msgbox("A whisper tells you to run. Don't fight that thing.")
            i = input("Fight, or flee?").lower
            if i == "fight":
                easygui.msgbox("The Mooshroom flipping demolishes you.")
                dead
            elif i == "flee":
                easygui.msgbox("Good choice, you continue on your way")

    if x == "7,9":
        p = input("You found a large mushroom with a hole in it, will you reach in?\n:").lower
        if p == "yes":
            easygui.msgbox("You slowly reach in ")
            easygui.msgbox("You feel something squishy.")
            o = input("Will you pick up the squishy mysterious object\n:").lower
            if o == yes:
                easygui.msgbox("You aquire an intelligence potion.")
                u = input("Will you drink it?").lower
                if u == "yes":
                    easygui.msgbox("You gain 2 intelligence")
                    intelligence + 2 = intelligence
                elif u == "no":
                    easygui.msgbox("Ok...")
                    easygui.msgbox("Idiot.")
        if p == "no":
            easygui.msgbox("WHY WOULDNT YOU GIVE ER A TRY?")
            easygui.msgbox("You are so lame.")

    if x == "10":
        easygui.msgbox("A bush rustles in the distance.")
        f = input("Will you go up to the bush\n:").lower
        if f == "yes":
            easygui.msgbox("A wild zigazoon jumps out.")
            a = input("Fight or flee?\n:").lower
            if a == "fight":
                easygui.msgbox("You slaughter that little racoon, with one swing of your arm.")
            if a == "flee":
                easygui.msgbox("You successfully flee from the scary little racoon")
        if f == "no":
            easygui.msgbox("Well arent you lame.")

    w = random.randrange(1,11)
    if w == "1,7":
        easygui.msgbox("You walk into a tree.")
        q = random.randrange(1,11)
        if q == "1,7":
            easygui.msgbox("A bright red dead eagle.")
            z = input("Will you poke it with a stick?\n:").lower
            if z == "yes":
                easygui.msgbox("The eagle has a final spasm before the body is dead and scratches your leg.")
                hp - 1 = hp
            if z == "no":
                easygui.msgbox("You carry on with your merry way.")
        if q == "8,10":
            easygui.msgbox("A bright blue eagle flys our of the tree and takes a shit on you.")
            hp - 1 = hp
            easygui.msgbox("It turns out, that there was 50 gold in it though.")
            gp + 50 = gp
    if w == "8,10":
        easygui.msgbox("You approach a molding mushroom.")
        qu = input("Will you go anywhere near it?\n:")
        if qu == "yes":
            easygui.msgbox("Ew, it smells.")
            j = input("Will you poke it with a stick?\n:").lower
            if j == "yes":
                easygui.msgbox("You have now contracted aids.")
                hp - 3 = hp
            easygui.msgbox("Oof.")
        if j == "no":
            easygui.msgbox("You inhale the fumes.")
            hp - 1 = hp
            easygui.msgbox("But wait, it seems that the fumes have ")
'''
character()
town()
#forest()
#mooshroom()
#cave()