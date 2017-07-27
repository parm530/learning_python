# write a tipper program where user enters a resteraunt bill total
# program should enter two values: a 15% tip and a 20% tip

cost =  int(input("Enter your bill cost: "))
tip1 = cost * .15
tip2 = cost * .20

print("A 15% tip is ", tip1)
print("A 20% tip is", tip2)

input("\n\nPress enter key to exit.")
