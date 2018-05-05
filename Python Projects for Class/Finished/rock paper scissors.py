import random

print("Let's play rock, paper, scissors")
bestof = int(int((input("\nbest of?\n")))/2) + 1
runs = 0
winTotal = 0
lossTotal = 0
print("run",bestof)
while runs <= bestof:
    choice = input("\nrock, paper, or scissors?\n")
    rps = 0
    win = 0

    try:
        if choice == 'rock' or choice == 'r':
            rps = 1
            print(choice)
        elif choice == 'paper' or choice == 'p':
            rps = 2
            print(choice)

        elif choice == 'scissors' or choice == 's':
            rps = 3
            print(choice)

    except:
        print("That is not an option!")

    if rps == 1:
        print("\nYou chose rock")
    elif rps == 2:
        print("\nYou chose paper")
    elif rps == 3:
        print("\nYou chose scissors")

    npc = random.randrange(1,4)

    if npc == 1:
        print("The computer chose rock\n")
    elif npc == 2:
        print("The computer chose paper\n")
    else:
        print("The computer chose scissors\n")

    if npc == rps:
        print("Tie!")
        runs -= 1
        win = 2
    elif npc == 1 and rps != 1:  #rock
        if rps == 2:
            print("Paper beats rock")
            win = 1
            winTotal += 1
        else:
            print("Rock beats scissors")
            lossTotal += 1

    elif npc == 2 and rps != 2:  #paper
        if rps == 1:
            print("Paper beats rock")
            lossTotal += 1
        else:
            print("Scissors beats paper")
            win = 1
            winTotal += 1

    else:           #scissors
        if rps == 1:
            print("Rock beats scissors")
            win = 1
            winTotal += 1
        else:
            print("Scissors beats paper")
            lossTotal += 1


    if win == 1:
        print("You won!")
    elif win ==2:
        print("")
    else:
        print("You lost!")

    runs += 1
    print(runs)
print("\nGG")
if winTotal > lossTotal:
    print("Congrats")
else:
    print("You are a failure")