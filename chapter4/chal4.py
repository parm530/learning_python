# Write a program where the computer picks a random word and the user has to
# try and guess the word
# The computer tells the user how many letters are in the words
# The user gets 5 chances to ask if a certain letter is in the word
# The computer responds by saying yes or no
# Then the player must guess the word

import random

WORDS = ("exercise",
         "fruit",
         "birthday",
         "education")

word = random.choice(WORDS)
counter = 0
allow = True

print("""
        Welcome to 'Guess The Word'

    Guess a random word that the computer generates!
    You have a maximum of 5 chances to ask if a letter is within the word!

    """)
print("\nThe word I am thinking about has", len(word), "letters.")
guess = input("\nTake a guess: ")

while guess != word:
    print("\nSorry, try again!")

    if allow:
        hint = input("Would you like 5 chances to guess letters? (Y/N)")
        
        if hint.lower() == "y":
            allow = False
            while counter < 5:
                letter = input("\nType a letter to see if it is in the word: ")
                if letter != "" and letter in word:
                    print("Yes!")
                else:
                    print("No")
                counter += 1
            print("\nYou must guess the word now!")
            guess = input("Final attempt: ")
            if guess != word:
                print("Sorry, that is not the word!")
                break
        else:
            guess = input("Take a guess: ")

if guess == word:
    print("\nCorrect! That's the word!")
    
print("\nThanks for playing!")
input("\nPress the enter key to exit.")
