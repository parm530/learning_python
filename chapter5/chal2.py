# Write a program that allows the user to allot 30 points
# to four attributes: strength, health, wisdom and dexterity


pool = 30
attributes = {"strength": 0,
              "health": 0,
              "wisdom": 0,
              "dexterity": 0}
b_val = True

print("\tCREATE A CHARACTER")

while b_val:
  user = input("""
    Select from the menu choice:
        A - Assign points to Characters
        C - Check attributes
        P - Put points back in to Pool
        E - Exit the game
        """ )
  if user.upper() == "A":
    for attribute in attributes:
      print("Attribute: %s" % attribute)
      point = int(input("Points: "))
      while pool - point < 0:
        print("\nCurrent Pool points: %s" %pool)
        point = int(input("\nEnter a valid point amount: "))
      attributes[attribute] = point
      pool -= point
      print("\nCurrent Pool points: %s" %pool)
  elif user.upper() == "C":
    print(attributes)
  elif user.upper() == "P":
    opt = True
    while opt:
      attr = input("\nWhich attribute will you remove points from? (Enter X to leave this menu): ")
      if attr.upper() == "X":
        opt = False
      else:
        while attr not in attributes:
          attr = input("\nEnter a valid atttribute:")
        val = int(input("\nHow many points will you remove?: "))
        while attributes[attr] - val < 0:
          val = int(input("\nEnter a valid point amount: "))
        attributes[attr] -= val
        pool += val
        print("\nCurrent %s points: %s" % (attr, attributes[attr]))
        print("\nCurrent Pool points: %s" %pool)

  elif user.upper() == "E":
    b_val = False



