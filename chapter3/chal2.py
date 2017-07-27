# write a program that flips a coin 100 times and then tells you the number of heads and tails


import random

heads = 0
tails = 0
counter = 0

while counter < 100:
    val = random.randint(0,1)
    if val == 0:
        heads += 1
    else:
        tails += 1
    counter += 1

print("Heads:" , heads, "Tails:", tails)

input("\nPress enter key to exit")
