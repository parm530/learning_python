# reverse the guessing game so that the computer has to guess the number
import random

print("\tWelcome to 'Guess My Number!'")

user = int(input("Pick a number for the Computer to guess, between 1 and 100:"))

comp = random.randint(1, 100)
tries = 1

while comp != user:
    if comp > user:
        comp  = random.randint(1, comp-1)
    else:
        comp = random.randint(comp+1, 100)
    tries += 1

print("The computer guessed your number", user, "in", tries, "tries!")
    
