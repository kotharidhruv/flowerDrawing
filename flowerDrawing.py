import turtle
import tkinter.messagebox as messagebox
 
 
painter = turtle.Turtle()
screen = turtle.screensize()

flowers = ["rose", "roses","daisy","daisies", "sunflower", "sunflowers","tulip","tulips","lily", "lilies", "tulip","tulips"]

flowerType = None
flowerNum = None

while flowerType is None and flowerNum is None:
    userInp = turtle.textinput("Flower Drawing", "Please enter the type of flower you want and the number of flowers. (ex. rose 3): ")
    words = userInp.split()
    for word in words:
        if word.lower() in flowers:
            flowerType = word.lower()
        elif word.isdigit():
            flowerNum = int(word)

    if flowerType is None or flowerNum is None:
        messagebox.showinfo("Error", "Please enter a valid flower type and number of flowers.")
    else:
        painter.speed(1)

if flowerNum>2:
    painter.speed(100)

def drawRose(scale):
    painter.penup ()
    painter.left (90)
    painter.fd (scale*200)
    painter.pendown ()
    painter.right (90)

    painter.fillcolor ("red")
    painter.begin_fill ()
    painter.circle (scale*10,180)
    painter.circle (scale*25,110)
    painter.left (50)
    painter.circle (scale*60,45)
    painter.circle (scale*20,170)
    painter.right (24)
    painter.fd (scale*30)
    painter.left (10)
    painter.circle (scale*30,110)
    painter.fd (scale*20)
    painter.left (40)
    painter.circle (scale*90,70)
    painter.circle (scale*30,150)
    painter.right (30)
    painter.fd (scale*15)
    painter.circle (scale*80,90)
    painter.left (15)
    painter.fd (scale*45)
    painter.right (165)
    painter.fd (scale*20)
    painter.left (155)
    painter.circle (scale*150,80)
    painter.left (50)
    painter.circle (scale*150,90)
    painter.end_fill ()
    
    # Petal 1
    painter.left (150)
    painter.circle (scale*-90,70)
    painter.left (20)
    painter.circle (scale*75,105)
    painter.setheading (60)
    painter.circle (scale*80,98)
    painter.circle (scale*-90,40)
    
    # Petal 2
    painter.left (180)
    painter.circle (scale*90,40)
    painter.circle (scale*-80,98)
    painter.setheading (-83)
    
    # Leaves 1
    painter.fd (scale*30)
    painter.left (90)
    painter.fd (scale*25)
    painter.left (45)
    painter.fillcolor ("green")
    painter.begin_fill ()
    painter.circle (scale*-80,90)
    painter.right (90)
    painter.circle (scale*-80,90)
    painter.end_fill ()
    painter.right (135)
    painter.fd (scale*60)
    painter.left (180)
    painter.fd (scale*85)
    painter.left (90)
    painter.fd (scale*80)
    
    # Leaves 2
    painter.right (90)
    painter.right (45)
    painter.fillcolor ("green")
    painter.begin_fill ()
    painter.circle (scale*80,90)
    painter.left (90)
    painter.circle (scale*80,90)
    painter.end_fill ()
    painter.left (135)
    painter.fd (scale*60)
    painter.left (180)
    painter.fd (scale*60)
    painter.right (90)
    painter.circle (scale*200,60)

def drawDaisy(scale):
    painter.pendown()
    def drawPetal(radius):
        painter.circle(radius, 60)
        painter.left(120)
        painter.circle(radius, 60)
        painter.left(120)

    radius = scale*80
    petals = 6

    for i in range(petals):
        drawPetal(radius)
        painter.left(360/petals)

    # Draw a yellow circle in the middle of the daisy
    painter.penup()
    painter.fillcolor("yellow")
    painter.begin_fill()
    painter.goto(painter.position()[0], painter.position()[1]-radius/5)
    painter.circle(radius/5)  # adjust the size as needed
    painter.end_fill()
    painter.pendown()

def drawSunflower(scale):
    painter.pendown()
    def drawPetal(radius):
        painter.fillcolor("yellow")
        painter.begin_fill()
        painter.circle(radius, 60)
        painter.left(120)
        painter.circle(radius, 60)
        painter.left(120)
        painter.end_fill()
    
    radius = scale*80
    petals = 6

    for i in range(petals):
        drawPetal(radius)
        painter.left(360/petals)

    painter.penup()
    painter.fillcolor("#5C4033")
    painter.begin_fill()
    painter.goto(painter.position()[0], painter.position()[1]-radius/5)
    painter.circle(radius/5)
    painter.end_fill()
    painter.pendown()

def drawTulip(scale):
    painter.penup ()
    painter.left (90)
    painter.fd (scale*200)
    painter.pendown ()
    painter.right (90)

    painter.fillcolor ("#64447c")
    painter.begin_fill ()
    painter.circle (scale*10,180)
    painter.circle (scale*25,110)
    painter.left (50)
    painter.circle (scale*60,45)
    painter.circle (scale*20,170)
    painter.right (24)
    painter.fd (scale*30)
    painter.left (10)
    painter.circle (scale*30,110)
    painter.fd (scale*20)
    painter.left (40)
    painter.circle (scale*90,70)
    painter.circle (scale*30,150)
    painter.right (30)
    painter.fd (scale*15)
    painter.circle (scale*80,90)
    painter.left (15)
    painter.fd (scale*45)
    painter.right (165)
    painter.fd (scale*20)
    painter.left (155)
    painter.circle (scale*150,80)
    painter.left (50)
    painter.circle (scale*150,90)
    painter.end_fill ()
    
    # Petal 1
    painter.left (150)
    painter.circle (scale*-90,70)
    painter.left (20)
    painter.circle (scale*75,105)
    painter.setheading (60)
    painter.circle (scale*80,98)
    painter.circle (scale*-90,40)
    
    # Petal 2
    painter.left (180)
    painter.circle (scale*90,40)
    painter.circle (scale*-80,98)
    painter.setheading (-83)
    
    # Leaves 1
    painter.fd (scale*30)
    painter.left (90)
    painter.fd (scale*25)
    painter.left (45)
    painter.fillcolor ("green")
    painter.begin_fill ()
    painter.circle (scale*-80,90)
    painter.right (90)
    painter.circle (scale*-80,90)
    painter.end_fill ()
    painter.right (135)
    painter.fd (scale*60)
    painter.left (180)
    painter.fd (scale*85)
    painter.left (90)
    painter.fd (scale*80)
    
    # Leaves 2
    painter.right (90)
    painter.right (45)
    painter.fillcolor ("green")
    painter.begin_fill ()
    painter.circle (scale*80,90)
    painter.left (90)
    painter.circle (scale*80,90)
    painter.end_fill ()
    painter.left (135)
    painter.fd (scale*60)
    painter.left (180)
    painter.fd (scale*60)
    painter.right (90)
    painter.circle (scale*200,60)

def drawLily(scale):
    painter.pendown()
    def drawPetal(radius):
        painter.fillcolor("yellow")
        painter.begin_fill()
        painter.circle(radius, 60)
        painter.left(120)
        painter.circle(radius, 60)
        painter.left(120)
        painter.end_fill()
    
    radius = scale*80
    petals = 6

    for i in range(petals):
        drawPetal(radius)
        painter.left(360/petals)

    painter.penup()
    painter.fillcolor("#5C4033")
    painter.begin_fill()
    painter.goto(painter.position()[0], painter.position()[1]-radius/5)
    painter.circle(radius/5)
    painter.end_fill()
    painter.pendown()


if flowerType=='rose' or flowerType=='roses':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawRose(1/flowerNum)
        painter.setheading(0)

elif flowerType=='daisy'or flowerType=='daisies':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawDaisy(1/flowerNum)
        painter.setheading(0)

elif flowerType=='sunflower' or flowerType=='sunflowers':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawSunflower(1/flowerNum)
        painter.setheading(0)

elif flowerType=='tulip' or flowerType=='tulips':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawTulip(1/flowerNum)
        painter.setheading(0)

elif flowerType=='lily' or flowerType=='lilies':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawLily(1/flowerNum)
        painter.setheading(0)

turtle.done()
