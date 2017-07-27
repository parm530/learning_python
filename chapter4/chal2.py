# write a program that accepts a message from the user and returns it backwards

message = input("Enter a message:")
backwards = ""

for i in range(len(message)-1, -1, -1):
    backwards += message[i]

print("Your message backwards is:", backwards)

input("\nPress the enter key to exit.")
