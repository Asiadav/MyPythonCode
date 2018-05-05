import math


def sqrt(userInput):
    theGuess = 0
    guess = 1
    goodGuess = 1
    root = 0
    mult = 1
    up = 0
    if userInput < 1:
        while userInput < 1:
            mult = mult * 10
            userInput = userInput * mult
        up = 1

    if userInput >= 1:
        while guess <= userInput:
            theGuess += 1
            guess = theGuess ** 2
            if guess == userInput:
                root = guess
                break
            if guess < userInput:
                goodGuess = guess
                if guess > userInput:
                    break

    for i in range(1000):
        x = (userInput - goodGuess) / (2 * theGuess)
        #print(x)
        x = x - x ** 2
        theGuess = theGuess + x
        goodGuess = theGuess ** 2
    root = x + theGuess

    if up == 1:
        root = sqrt(10) * root / mult

    return root
x = float(input(''))
print(sqrt(x))
print(math.sqrt(x))
print(sqrt(x)**2)


