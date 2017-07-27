# write a program that counts for the user:
#   the user enters the starting number, ending number and number by which
#   to count

start = int(input("Enter a starting number:"))
end = int(input("Enter a number to end at: "))
count_by = int(input("Enter a number to step the count by: "))

for i in range(start, end, count_by):
    print(i)

input("\n\nPress the enter key to exit.")
