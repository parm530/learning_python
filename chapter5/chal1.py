# Create a program that prints a list of words in random order
# The program should print all the words and not repeat any

import random

words = ["Hello", "Bye", "Hi", "Welcome", "Enjoy"]

while words:
  word = random.choice(words)
  print(word)
  words.remove(word)

