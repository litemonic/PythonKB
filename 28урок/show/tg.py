"""
Данный код будет визуализировать треугольник с найденным тангенсом
"""
def ShowTg(AC, CB, res):
    import turtle
    turtle.hideturtle()
    turtle.color("white")
    turtle.bgcolor("black")
    turtle.title("нахождение tg")
    turtle.setup(500, 500)
    
    turtle.begin_fill()
    turtle.forward(AC * 10)
    turtle.right(90)
    turtle.forward(CB * 10)
    turtle.home()
    turtle.end_fill()

    turtle.penup()
    turtle.backward(AC * 10 - 50)
    turtle.pendown()
    turtle.color("white")
    turtle.write(f"tg = {res}", font=('Lato Light', 30, 'normal'))
    turtle.done()