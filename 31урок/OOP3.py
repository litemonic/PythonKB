import turtle
class Turtle:
    def __init__(self, color, width_of_line):
        self.color = color
        self.width_of_line = width_of_line
    def print_rectangle(self):
        if self.color and self.width_of_line:
            turtle.color = self.color
            turtle.pensize = self.width_of_line
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
        else:
            return "цвет или размер не выбраны."
    def print_triangle(self):
        if self.color and self.width_of_line:
            turtle.color = self.color
            turtle.pensize = self.width_of_line
            turtle.forward(100)
            turtle.right(120)
            turtle.forward(100)
            turtle.right(120)
            turtle.forward(100)
        else:
            return "цвет или размер не выбраны."
            

while True:
    command = input("Что вы хотите сделать? (1 - нарисовать квадрат, 2 - нарисовать треугольник, 3 - выход)")
    match command:
        case "1":
            color = input("Введите цвет квадрата: ")
            width = input("Введите толщину квадрата: ")
            cherepashka1 = Turtle(color, width)
            cherepashka1.print_rectangle()
        case "2":
            color = input("Введите цвет треугольника: ")
            width = input("Введите толщину треугольника: ")
            cherepashka2 = Turtle(color, width)
            cherepashka2.print_triangle()
        case "3":
            print("Программа завершена: ")
            break
        case _:
            print("Неизвестная команда")