import turtle

def drawSquare(t, sideLength):
    for i in range(4):
        t.forward(sideLength)
        t.left(90)

def movement():
    window = turtle.Screen()
    window.bgcolor("red")
    t = turtle.Turtle()
    t.forward(100)
    t.left(10)
    t.forward(100)
    window.exitonclick()

def drawFigure(sideLength):
    window = turtle.Screen()
    window.bgcolor("red")
    t = turtle.Turtle()
    for i in range(72):
        drawSquare(t, sideLength)
        t.left(5)
    window.exitonclick()

def drawHexagon(sideLength):
    window = turtle.Screen()
    window.bgcolor("red")
    t = turtle.Turtle()
    for i in range(6):
        for j in range(2):
            t.forward(sideLength)
            t.left(120)
        t.forward(sideLength)
        t.left(180)
    window.exitonclick()

def drawOctagon():
    window = turtle.Screen()
    window.bgcolor("red")
    t = turtle.Turtle()
    t.forward(100)
    t.speed(0)
    for i in range(7):
        t.left(45)
        t.forward(100)
    window.exitonclick()

def drawFlowerPetal(t, sideLength):
    for i in range(2):
        t.forward(sideLength)
        t.left(60)
        t.forward(sideLength)
        t.left(120)

def drawFlower(sideLength):
    window = turtle.Screen()
    window.bgcolor("red")
    t = turtle.Turtle()
    t.speed(0)
    for i in range(72):
        drawFlowerPetal(t, sideLength)
        t.left(5)

    t.right(90)
    t.forward(300)

    window.exitonclick()

def drawNameInitials():
    window = turtle.Screen()
    window.bgcolor("red")
    t = turtle.Turtle()

    t.speed(0)
    t.setposition(-200, 0)
    t.left(60)
    t.forward(200)
    t.backward(200)
    t.left(60)
    t.forward(200)
    t.backward(200)
    t.right(120)

    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.forward(86)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(86)
    t.right(90)
    t.forward(200)

    window.exitonclick()

def twoTurtles():
    window = turtle.Screen()
    window.bgcolor("red")

    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t2.left(180)

    t1.forward(50)
    t2.forward(50)
    t1.left(90)
    t2.right(90)
    t1.forward(100)
    t2.forward(100)
    t1.left(90)
    t2.right(90)
    t1.forward(50)
    t2.forward(50)

    window.exitonclick()

def drawTriangle(side):
    window = turtle.Screen()
    window.bgcolor("red")

    t = turtle.Turtle()
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    window.exitonclick()


#drawFigure(100)
#drawHexagon(100)
#drawOctagon()
#twoTurtles()
#drawFlower(100)
#drawNameInitials()
drawTriangle(100)