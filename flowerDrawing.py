import turtle as trtl

painter = trtl.Turtle()

flowers = ["rose", "daisy", "sunflower", "tulip","lily", "magnolia", "violet", "cosmos", "lily", "rose", "sunflower", "tulip"]

userInp = input("Please enter the type of flower you want and the number of flowers. (ex. rose 3): ")
flowerType = userInp.split()[0]
flowerNum = int(userInp.split()[1])


color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
width = 400
height = 300

angle = int(input("angle:"))
seg = int(360/angle)
space=0

while painter.ycor() < height:
    if painter.pencolor() == color2:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1

while painter.ycor() < height:
    if painter.pencolor() == color2:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1