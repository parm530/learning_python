# write a orgram that simulates a fortune cookie
# should display 1 of 5 random fortunes each time it is run

import random

fortune = random.randint(1, 5)

if fortune == 1:
    print("You will recieve lots of wealth soon!")
elif fortune == 2:
    print("Today will be a bad day for you, keep up a positive attitude!")
elif fortune == 3:
    print("Spend time with loved ones today.")
elif fortune == 4:
    print("Despite the road block in your life, soon you will achieve success!")
else:
    print("You will succeed in all your goals!")
    
input("\n\nPress the enter key to exit")
