import turtle,math

def drawPistil(pen):
    length = 2 * pistilRadius * math.cos((180 - angle) * math.pi / 180)
    for i in range(180 / (2 * angle - 180)):
        pen.forward(pistilRadius)
        drawPetal(pen)
        pen.right(angle)
        pen.forward(length)
        pen.right(angle)
        pen.forward(pistilRadius)

def drawPetal(petalPen):
    lastPosition = petalPen.position()
    lastHeading = petalPen.heading()
    length = 100
    petalAngle = 60
    petalPen.right(petalAngle)
    petalPen.forward(length)
    petalPen.right(petalAngle * 2)
    petalPen.forward(length)
    petalPen.back(length)
    petalPen.left(petalAngle * 2)
    petalPen.back(length)
    petalPen.left(petalAngle)
    petalPen.setposition(lastPosition)
    petalPen.setheading(lastHeading)
    

window = turtle.Screen()
window.bgcolor('green')

magicPen = turtle.Turtle()
magicPen.shape('turtle')
magicPen.color('red')
magicPen.speed(30)


pistilRadius = 100
pistilAngle = 5
angle = 180 - (180 - pistilAngle) / 2

drawPistil(magicPen)
magicPen.home()
magicPen.setheading(180)
magicPen.forward(300)


window.exitonclick()
