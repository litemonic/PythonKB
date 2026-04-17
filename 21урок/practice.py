import turtle

print("Данная программа рисует геометрические фигуры")
print("Перед тем как приступить поработаем надо оформлением")
choice1 = input("Изначально фон белый. Хотите его поменять? (да/нет): ").lower().strip()
if choice1 in ["да", "д", "yes", "y"]:
    try:    
        bgInput = input("Напишите свой цвет на англ: ")
        turtle.bgcolor = bgInput
    except Exception as e:
        print("Error! Действие не выполнено.")
    choice3 = input("""Какую фигуру хотите видеть?
1.Квадрат
2.Круг  
""")
    if choice3 == "1":
        choice2 = input("\nПойдем дальше. Желаете закрасить фигуру? (да/нет): ")
        if choice2 in ["да", "д", "yes", "y"]:
            fillFigure = input("Напишите свой цвет на англ: ")
            turtle.fillcolor(fillFigure)