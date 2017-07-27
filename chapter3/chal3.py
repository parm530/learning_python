# edit the Guess my number game to give the player a limited amount of guesses
# once the guess count is met, give a message

print("\tWelcome to 'Guess My Number!'")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 5 attempts.\n")


import random

the_number = random.randint(1,100)
print(the_number)
guess = int(input("Take a guess:"))
tries = 1

while tries < 5 and guess != the_number:
        if guess < the_number:
            print("Higher ...")
        else:
            print("Lower ...")
        guess = int(input("Take a guess:"))
        tries += 1
        
if guess == the_number:
    print("Thats it! You guessed the number", the_number)
else :
    print("Sorry, you weren't able to guess the number!")
    
print("\nPress the enter key to exit.")


