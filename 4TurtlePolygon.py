import turtle
wn = turtle.Screen()
kermit = turtle.Turtle()

number_of_sides = int(input("Enter number of sides."))
length_of_sides = int(input("Enter length of side."))
kermit_side_color = input("Enter color of side.")
kermit_color = input("Enter fillcolor.")

kermit.begin_fill()
for i in range(number_of_sides):
    kermit.color(kermit_color)
    kermit.pencolor(kermit_side_color)
    kermit.forward(length_of_sides)
    kermit.left(360/number_of_sides)
kermit.end_fill()
