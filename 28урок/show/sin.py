"""
Данный код будет визуализировать треугольник с найденным синусом
"""
def ShowSin(AC, CB, res):
    import turtle
    turtle.hideturtle()
    turtle.color("red")
    turtle.bgcolor("black")
    turtle.title("нахождение sin")
    turtle.setup(500, 500)

    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(AC * 10)
    turtle.left(90)
    turtle.forward(CB * 10)
    turtle.home()
    turtle.end_fill()
    
    turtle.penup()
    turtle.backward(AC * 10 - 50)
    turtle.pendown()
    turtle.color("white")
    turtle.write(f"sin = {res}", font=('Lato Light', 30, 'normal'))
    turtle.done()