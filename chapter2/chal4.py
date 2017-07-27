# write a car salesman program where the user enters a base price for a car
# program should add on a bunch of prices on to the base price
# tax and license should be a percentage of the base price
# display the actual price once all the fees have been added

car_cost = int(input("What is the price of the car?"))
tax = car_cost * .20
license_cost = car_cost * .12
dealer = 1500

final_cost = car_cost + tax + license_cost + dealer
print(final_cost)
input("\n\nPress the enter key to exit.")
