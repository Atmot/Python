# Calculates MPG for a car

miles_driven_str = input("Please enter the amount of miles driven.")
miles_driven = int(miles_driven_str)

gallons_used_str = input("Please enter the number of gallons used.")
gallons_used = int(gallons_used_str)

MPG = miles_driven / gallons_used

print("You used", MPG, "miles per gallon.")


