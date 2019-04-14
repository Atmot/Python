# Calculates the area of a circle

radius_str = input("Please input the radius of your circle (in cm)")
radius = int(radius_str)

import math

area = math.pi * radius**2

print("The area of your circle is", area, "square cms.")
