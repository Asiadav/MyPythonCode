import random

heads = 0
tails = 0

for i in range(50):
    flip = random.randrange(0,2)
    if flip == 1:
        print("heads")
        heads += 1

    else:
        print("tails")
        tails += 1
print("\nheads:",heads)
print("tails:",tails)

print("\nratio:")
print(heads/tails)