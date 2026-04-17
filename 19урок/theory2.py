import turtle
turtle.shape('turtle')
turtle.speed(0) # 0 - макс значение, 10 - мин значение
turtle.bgcolor("black")



def move():
    turtle.forward(10)
def turnLeft():
    turtle.left(15)
def turnRight():
    turtle.right(15)
def backMove():
    turtle.backward(10)
def clearScreen():
    turtle.clear()
def up():
    turtle.penup
def dw():
    turtle.pendown
turtle.listen()
turtle.onkey(move, "Up")
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnRight, "Right")
turtle.onkey(backMove, "Down")
turtle.onkey(clearScreen, "c")
turtle.onkey(up, "v")
turtle.onkey(dw, "b")

turtle.done()

