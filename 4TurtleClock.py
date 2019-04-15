import turtle
wn = turtle.Screen()
pin = turtle.Turtle()

pin.shape("turtle")
wn.bgcolor("light green")
pin.color("blue")
pin.stamp()

for i in range(12):
    pin.pensize(3)
    pin.penup()
    pin.forward(70)
    pin.pendown()
    pin.forward(10)
    pin.penup()
    pin.forward(20)
    pin.stamp()
    pin.forward(-100)
    pin.left(360/12)
