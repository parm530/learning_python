# Write a Who's Your Daddy program that lets the user
# enter the name of a male and produces the name of 
# of his father
# Allow the user to add, replace and delete son-father pairs
# EDIT: Allows the user to look up the Grandfather of the son

import random

fathers = { "Kishan": ["Deonarine", "Grampa Sahadeo"],
            "Jayden": ["Will", "Grampa Smith"]
            }

print("""
    Who's Your Daddy?
    """)

bool_v = True

while bool_v:
  user = input("""
    Choose from the menu options:
      L = Looks up the name of the father
      A = Adds a son-father pair
      R = Edits the son-father pair
      D = Deletes the son-father pair
      G = Looks up the grandfather
      X = Exits the program
      """)
  if user.upper() == "L":
    son = input("\nEnter the son's name to find his father: ")
    if son in fathers:
      print(fathers[son][0])
    else:
      print("\nSorry, could not find %s's father." %son)

  elif user.upper() == "A":
    son_name = input("\nEnter the son's name: ")
    father_name = input("\nEnter his father's name: ")
    fathers[son_name][0] = father_name

  elif user.upper() == "R":
    son_name = input("\nWhich son will you change his father?: ")
    if son_name in fathers:
      fathers[son_name][0] = input("\nEnter his new father's name: ")
    else:
      print("Sorry, %s is not found, go to the menu and press A to add a son." %son_name)
  elif user.upper() == "D":
    son_name = input("\nEnter the name of the son that you wish to remove: ")
    if son_name in fathers:
      del fathers[son_name]
    else:
      print("\nSorry, could not find %s" %son_name)

  elif user.upper() == "G":
    son_name = input("\nEnter the name of the son whose grandfather you wish to know: ")
    if son_name in fathers:
      print("%s's grandfather is %s" %(son_name, fathers[son_name][1]))
      
  elif user.upper() == "X":
    bool_v = False