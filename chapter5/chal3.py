# Write a Who's Your Daddy program that lets the user
# enter the name of a male and produces the name of 
# of his father
# Allow the user to add, replace and delete son-father pairs

import random

fathers = { "Kishan": "Deonarine",
            "Jayden": "Will"
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
      X = Exits the program
      """)
  if user.upper() == "L":
    son = input("\nEnter the son's name to find his father: ")
    if son in fathers:
      print(fathers[son])
    else:
      print("\nSorry, could not find %s's father." %son)

  elif user.upper() == "A":
    son_name = input("\nEnter the son's name: ")
    father_name = input("\nEnter his father's name: ")
    fathers[son_name] = father_name

  elif user.upper() == "R":
    son_name = input("\nWhich son will you change his father?: ")
    if son_name in fathers:
      fathers[son_name] = input("\nEnter his new father's name: ")
    else:
      print("Sorry, %s is not found, go to the menu and press A to add a son." %son_name)
  elif user.upper() == "D":
    son_name = input("\nEnter the name of the son that you wish to remove: ")
    if son_name in fathers:
      del fathers[son_name]
    else:
      print("Sorry, could not find %s" %son_name)
      
  elif user.upper() == "X":
    bool_v = False