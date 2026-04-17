"""
Данный код будет визуализировать треугольник с найденным косинусом
"""
def ShowCos(CB, AB, res):
    import turtle
    turtle.hideturtle()
    turtle.color("green")
    turtle.bgcolor("black")
    turtle.title("нахождение cos")
    turtle.setup(500, 500)
    
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(AB * 10)
    turtle.right(90)
    turtle.forward(CB * 10)
    turtle.home()
    turtle.end_fill()

    turtle.penup()
    turtle.backward(CB * 10 - 50)
    turtle.pendown()
    turtle.color("white")
    turtle.write(f"cos = {res}", font=('Lato Light', 30, 'normal'))
    turtle.done()