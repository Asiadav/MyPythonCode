import random
import time
points = 0

#Math Test

def mathTest(points):
    points = points
    print("playing quiz on Math")
    def q1(points):
        correct = "B"
        answer = input("\n\nEvaluate: 10 % 1.5\nA)0.5\nB)1.0\nC)1.5\nD)2.0\n")

        if answer.upper() == correct or answer == '1' or answer == '1.0':
            points = points + 7
            print("Correct!")

        if answer.upper() != correct and answer != '1' and answer != '1.0':
            print("Wrong!")

        return points


    def q2(points):
        correct = "C"
        answer = input("\n\nSolve: x**2 + 2x + 1 = 0\nA)1\nB)2\nC)-1\nD)-2\n")

        if answer.upper() == correct or answer == '1':
            points = points + 7
            print("Correct!")

        if answer.upper() != correct and answer != '1':
            print("Wrong!")

        return points



    def q3(points):
        correct = "A"
        answer = input("\n\nFind sin(x): cos(x) = 1\nA)0\nB)1/3\nC)1/2\nD)1\n")

        if answer.upper() == correct or answer == '0':
            points = points + 7
            print("Correct!")

        if answer.upper() != correct and answer != '0':
            print("Wrong!")

        return points



    def q4 (points):
        correct = "B"
        answer = input("\n\nSimplify: ((((x+1)-x**7)x*0)-1)*-1-1\nA)x\nB)0\nC)1\nD)x-1\n")

        if answer.upper() == correct or answer == '0':
            points = points + 7
            print("Correct!")

        if answer.upper() != correct and answer != '0':
            print("Wrong!")

        return points


    def q5(points):
        correct = "C"
        answer = input("\n\nHow many faces faces does a dodecahedron have?\nA)10\nB)11\nC)12\nD)13\n")

        if answer.upper() == correct or answer == '12':
            points = points + 7
            print("Correct!")

        if answer.upper() != correct and answer != '12':
            print("Wrong!")

        return points


    def q6(points):
        correct = "D"
        answer = input("\n\nWhich is best?\nA)Orthocenter\nB)Mid-Center\nC)Circumcenter\nD)Centroid\n")

        if answer.upper() == correct or answer.upper() == 'CENTROID':
            points = points + 7
            print("Correct!")

        if answer.upper() != correct and answer.upper() != 'CENTROID':
            print("Wrong!")

        return points
    from random import shuffle
    Qlist = [q1,q2,q3,q4,q5,q6]
    shuffle(Qlist)
    for i in range(6):
        points = Qlist.pop()(points)
        time.sleep(.25)
        #print(points)
    return points





#Will Smith

def will_smith_questions(points):
    userPoints = points
    print("playing quiz on Will Smith")
    correct = "C"
    answer = input("Question 1:\nHow long would it take Will Smith to solve a Rubiks Cube?\nA)He can’t solve rubiks cubes\nB)59 Seconds\nC)55 Seconds\nD)Will Smith can solve a rubiks cube instantly")

    if answer == correct:
        userPoints = userPoints + 7
        print("Correct!")

    if answer != correct:
        print("Wrong!")


    correct = "C"
    answer = input("Question 2:\nWhat movie did he most regret making?\nA)I robot\nB)Men in black II\nC)Wild Wild West\nD)Suicide Squad")

    if answer == correct:
        userPoints = userPoints + 7
        print("Correct!")

    if answer != correct:
        print("Wrong!")


    correct = "D"
    answer = input("Question 3:\nWhat game does Will Smith like?\nA)Poker\nB)Checkers\nC)CHINESE checkers\nD)Chess")

    if answer == correct:
        userPoints = userPoints + 7
        print("Correct!")

    if answer != correct:
        print("Wrong!")


    correct = "D"
    answer = input("Question 4:\nHow many kids does Will have?\nA)5\nB)He had no kids\nC)2\nD)3")

    if answer == correct:
        userPoints = userPoints + 7
        print("Correct!")

    if answer != correct:
                    print("Wrong!")


    correct = "C"
    answer = input("Question 5:\nAt what age did will smith become a millionaire?\nA)23\nB)55\nC)20\nD)All of the Above")

    if answer == correct:
            userPoints = userPoints + 7
            print("Correct!")

    if answer != correct:
            print("Wrong!")


    correct = "C"
    answer = input("Question 6:\nWhat language (other than english) is he fluent in?\nA)Swedish\nB)Japanese\nC)Spanish\nD)French")

    if answer == correct:
            userPoints = userPoints + 7
            print("Correct!")

    if answer != correct:
            print("Wrong!")

    return userPoints




#Computers

def computersTest(points):
    CorrectAnswerCounter = points

    #Question One
    print("Qu1: Is the standard Zotac 750ti sli ready?")
    answer_1 = input("A. Yes\nB. No\nC. Maybe-So\n:").lower()
    print(answer_1)
    if answer_1 == "b" or answer_1 == "no":
        print("Correct")
        CorrectAnswerCounter = CorrectAnswerCounter + 7
    else:
        print("Incorrect, It isn't.")

    print("Questions answered correct:")
    print(CorrectAnswerCounter)

    #Question Two
    print("Qu2: How many cuda cores are there in a gtx 1050ti?")
    answer_2 = input("A. 763\nB. 758\nC. 768\nD. 752\n:").lower()
    print(answer_2)
    if answer_2 == "c" or answer_2 == "768":
        print("Correct")
        CorrectAnswerCounter = CorrectAnswerCounter + 7
    else:
        print("Incorrect, You are an Imbecile")

    print("Questions answered correct:")
    print(CorrectAnswerCounter)

    #Question Three
    print("Qu3: What is the standard GDDR5 memory interface for a gtx 960?")
    answer_3 = input("A. 1\nB. 2\nC. 3\nD. 4\nE. All of the above\n:").lower()
    print(answer_3)
    if(answer_1) == "b" or answer_3 == "2":
        print("Correct")
        CorrectAnswerCounter = CorrectAnswerCounter + 7
    else:
        print("Incorrect, you bloody idiot.")

    print("Questions answered correct:")
    print(CorrectAnswerCounter)

    #Question Four
    print("Qu4: What is the length of Ash's right lense of his glasses?")
    answer_4 = input("A. 5cm\nB. 6cm\nC. 4.57cm\nD. 2.9cm\n").lower()
    print(answer_4)
    if answer_4 == "a" or answer_4 == "5cm":
        print("Correct")
        CorrectAnswerCounter = CorrectAnswerCounter + 7
    else:
        print("Incorrect, nice try butthead!")

    print("Questions answered correct:")
    print(CorrectAnswerCounter)

    #Question Five
    print("Qu5: What is the most bought item on amazon as of 1/31/2018")
    answer_5 = input("A. Amazon Echo Dot\nB. iPhone 7s\nC. Kindle Fire HD7\nD. Amazon Echo\n:").lower()
    print(answer_5)
    if answer_5 == "d" or answer_5 == "amazon echo":
        print("Correct")
        CorrectAnswerCounter = CorrectAnswerCounter + 7
    else:
        print("FALSE, it seems beavis has taken over.")

    print("Questions answered correctly")
    print(CorrectAnswerCounter)

    #Question Six
    print("Qu6: What is the recommended turbo boost on an AMD FX-8350")
    answer_6 = input("A. 4.2GHz\nB. 4.2MHz\nC. 6.7GHz\nD. 1.2MHz\n:").lower()
    print(answer_6)
    if answer_6 == "a" or answer_6 == "4.2GHz":
        print("You are a god damn genius")
        CorrectAnswerCounter = CorrectAnswerCounter + 7
    else:
        print("Stop being so wrong all the time.")

    print("Questions answered correctly")
    print(CorrectAnswerCounter)

    return CorrectAnswerCounter




#Minecraft

def minecraftTest(points):
    #question 1
    score = points
    print("How many obsidian blocks does it take to make an nether portal?")
    answer_1 = input("A. 10\nB. 14\nC. 16\nD. 18\n:").lower()
    print(answer_1)
    if answer_1 == "a" or answer_1 == "10":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect")
    print("Questions answered correctly:")
    print(score)

    #question 2
    print("How many hearts does steve start with?")
    answer_2 = input("A. 1\nB. 5\nC. 10\nD. 15\n:").lower()
    print(answer_2)
    if answer_2 == "c" or answer_2 == "10":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect")
    print("Questions answered correctly:")
    print(score)

    #question 3
    print("What was minecraft originally called?")
    answer_3 = input("A. Block Man\nB. Mine-It\nC. Cave Game\nD. Craft Blocks\n:").lower()
    print(answer_3)
    if answer_3 == "c" or answer_3 == "cave game":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect")
    print("Questions answered correctly:")
    print(score)

    #question 4
    print("Where is Markus Notch Perrson from?")
    answer_4 = input("A. Sweden\nB. Greece\nC. Germany\nD. Russia\n:").lower()
    print(answer_4)
    if answer_4 == "a" or answer_4 == "sweden":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect")
    print("Questions answered correctly:")
    print(score)

    #question 5
    print("What game features the notched pickaxe?")
    answer_5 = input("A. Meatal Gears\nB. Skyrim\nC. Overwatch\nD. Super Mario Odyssey\n:").lower()
    print(answer_5)
    if answer_5 == "c" or answer_5 == "skyrim":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect")
    print("Questions answered correctly:")
    print(score)

    #question 6
    print("The game was created in 6 days but how long until it was ready for release?")
    answer_6 = input("A. 1 year\nB. 2 years\nC. 3 years\nD. 5 years\n:").lower()
    print(answer_3)
    if answer_6 == "b" or answer_6 == "2 years":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect")
    print("Questions answered correctly:")
    print(score)

    return score



#Cartoons
def cartoonsTest(points):
    points = points


    print("playing quiz on Cartoons")
    answer = input("Question 1: Who sings the intro to Arthur?\nA. Will Smith\nB. Ziggy Marley\nC. Bruce Lee\nD. Nico Audy-Rowland\n:")

    if answer.upper() == "B" or answer.upper() == "ZIGGY MARLEY":
        points = points + 7
        print("Correct!")

    else:
        print("Wrong!")


    answer = input("Question 2: Who has been in almost every cartoon as a side guest character?\nA. Chris Pratt\nB. Bruce Lee\nC. 'Weird' Al Yankovic\nD. Trey Parker\n:")

    if answer.upper() == "C" or answer.upper() == "'WEIRD' AL YANKOVIC":
        points = points + 7
        print("Correct!")

    else:
        print("Wrong!")



    answer = input("Question 3: What was the name of Bruce Wayne’s dog in Batman Beyond?\nA. Jason Todd\nB. Killer\nC. Ace\nD. Bat-Hound\n:")

    if answer.upper() == "C" or answer.upper() == "ACE":
        points = points + 7
        print("Correct!")

    else:
        print("Wrong!")
    answer = input("Question 4: Which character automatically makes anything 20% cooler?\nA. Son Goku\nB. Rainbow Dash\nC. Han Solo\nD. Jotaro Kujo (Jojo's Bizarre Adventure)\n:")

    if answer.upper() == "B" or answer.upper() == "RAINBOW DASH":
        points = points + 7
        print("Correct!")

    else:
        print("Wrong!")



    answer = input("Question 5: In the original animated The Hobbit movie, what color were Bilbo’s socks when Gandalf came by?\nA. Black\nB. Yellow\nC. Green\nD. Salmon\n:")
    if answer.upper() == "C" or answer.upper() == "GREEN":
            points = points + 7
            print("Correct!")

    else:
            print("Wrong!")



    answer = input("Question 6: Which of these characters do NOT have a background story that was ripped off of Superman?\nA. Lion-O(Thundercats)\nB. Captain Underpants\nC. Ratchet(Ratchet and Clank)\nD. Ryuko Matoi(Kill La Kill)\n:")
    if answer.upper() == "D" or answer.upper() == "Ryuko Matoi":
            points = points + 7
            print("Correct!")

    else:
            print("Wrong!")

    return points


for i in range(6):
    if i >= 2 and points <= 0:
        print("\n YOU HAVE FAILED")
        break
    if i >= 3 and points <= 7:
        print("\n YOU HAVE FAILED")
        break
    if i >= 4 and points <= 14:
        print("\n YOU HAVE FAILED")
        break
    if i >= 5 and points <= 21:
        print("\n COGRADULATIONS! YOU WIN!")
        break
    time.sleep(.5)
    print("\nWhich quiz will you take?\n")
    choice = input("1) Math\n2) Will Smith\n3) Computers\n4) Minecraft\n5) Cartoons\n")
    if points == None:
        points = 0
    if choice == '1' or choice.upper() == 'MATH':
        points = mathTest(points)
        print("Your current score is:", points)

    if choice == '2' or choice.upper() == 'WILL SMITH':
        points = will_smith_questions(points)
        print("Your current score is:", points)

    if choice == '3' or choice.upper() == 'COMPUTERS':
        points = computersTest(points)
        print("Your current score is:", points)

    if choice == '4' or choice.upper() == 'MINECRAFT':
        points = minecraftTest(points)
        print("your current score is:", points)

    if choice == '5' or choice.upper() == 'CARTOONS':
        points = cartoonsTest(points)
        print("Your current score is:",points)
        #print("This Test is Currently Unavailable")

    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice.upper() != 'MATH' and choice.upper() != 'WILL SMITH' and choice.upper() != 'COMPUTERS' and choice.upper() != 'MINECRAFT' and choice.upper() != 'CARTOONS':
        print("That's not a valid input")
