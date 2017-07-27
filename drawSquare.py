import turtle


def drawSquare(pen):
    for i in range(4):
        pen.forward(100)
        pen.right(90)

def drawTriangle(pen):
    for i in range(3):
        pen.forward(100)
        pen.right(120)

def drawCircle(pen):
    pen.circle(100)


window = turtle.Screen()
window.bgcolor('green')

brad = turtle.Turtle()
brad.shape('turtle')
brad.speed(10)
brad.color('yellow')


brad.forward(100)
brad.right(90)
brad.forward(100)
#drawSquare(brad)
#drawCircle(brad)
#drawTriangle(brad)

window.exitonclick()

