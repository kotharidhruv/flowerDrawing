import turtle
 
 
painter = turtle.Turtle()
screen = turtle.screensize()

flowers = ["rose", "daisy", "sunflower", "tulip","lily", "magnolia", "violet", "cosmos", "lily", "rose", "sunflower", "tulip"]

userInp = input("Please enter the type of flower you want and the number of flowers. (ex. rose 3): ")
flowerType = userInp.split()[0]
flowerNum = int(userInp.split()[1])

painter.speed(1)

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

if flowerType=='rose':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawRose(1/flowerNum)

elif flowerType=='daisy':
    for i in range(flowerNum):
        print(f"i: {i}, screen[0]: {screen[0]}, 1/flowerNum: {1/flowerNum}")
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/flowerNum),0)
        print(f"painter position: {painter.position()}")
        drawDaisy(1/flowerNum)
