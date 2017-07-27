# Modify the Guess My Number game to include a main() function
# that contains the actual guessing game

import random

def ask_number(question = "Choose a number from 1 to 100: ", low = 1, high = 100):
  response = None
  while response not in range(low, high):
    response = int(input(question))
  return response 

def main():
  print("\tWelcome to 'Guess My Number!'")
  print("\nI'm thinking of a number between 1 and 100.")
  print("Try to guess it in 5 attempts.\n")

  the_number = random.randint(1,100)
  print(the_number)
  guess = ask_number()
  tries = 1

  while tries < 5 and guess != the_number:
          if guess < the_number:
              print("Higher ...")
          else:
              print("Lower ...")
          guess = ask_number()
          tries += 1
          
  if guess == the_number:
      print("Thats it! You guessed the number", the_number)
  else :
      print("Sorry, you weren't able to guess the number!")
      
  print("\nPress the enter key to exit.")

main()
