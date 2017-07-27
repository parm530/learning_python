# Improve the word jumble game to provide a hint if the player is stuck
# Add a scoring system that rewards the player if the hint is not used

import random

LANGS = ("python", "ruby", "javascript")
word = random.choice(LANGS)
correct = word
hint_recieved = False

jumbled = ""
while word:
    position = random.randrange(len(word))
    jumbled += word[position]
    word = word[:position] + word[(position+1):]

print( """
            Welcome to Word Jumble

        Unscramble the letters to reveal a word
""")

print("The jumbled word is:", jumbled)

guess = input("Take a guess:")

while guess != correct and guess != "":
    print("Sorry, that is incorrect!")
    
    hint = input("Would you like to recieve a hint? (Yes or No): ")
    if hint.lower() == "yes":
        hint_recieved = True
        if correct == "ruby":
            print("A language named after a gem")
        elif correct == "python":
            print("A language named after a snake")
        elif correct == "javascript":
            print("A scripting language named after a brand of coffee")
        guess = input("What is the word?: ")
    else:
        guess = input("Try again: ")
        

if guess == correct and not hint_recieved:
    print("That's it! You guessed it without a hint! Great job!!!")
elif guess == correct:
    print("That's it! You guessed it!")
        
print("Thanks for playing!")
input("\nPress the enter key to exit.")

