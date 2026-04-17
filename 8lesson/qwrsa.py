'''
исключения
try
except
num1 = float(input("1"))
num2 = float(input("2"))
operation = input("3")
try:
    if operation == '+':
        print(f"Результат: {num1} {operation} {num2} = {num1 + num2} ")
    elif operation == '-':
        print(f"Результат: {num1} {operation} {num2} = {num1 - num2} ")
    elif operation == '*':
        print(f"Результат: {num1} {operation} {num2} = {num1 * num2} ")
    elif operation == '/':
        print(f"Результат: {num1} {operation} {num2} = {num1 / num2} ")
    else:
        print("Команды нет")
except ZeroDivisionError:
    print("На ноль делить нельзя))")

'''
import math
print("Программа нахождения площади и периметра геометрических фигур.\n")

try:
    while True:
        action = input("Что вы хотите найти? (периметр или площадь): ").strip().lower()
        figure = input("Выберите фигуру (квадрат/прямоугольник/круг/равносторонний прямоугольный треугольник/треугольник): ").strip().lower()
        if action == "периметр":
                if figure == "квадрат":
                    side = int(input("Введите сторону квадрата: "))
                    print(f"Периметр равен: {side*4}")

                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                elif figure == "равносторонний прямоугольный треугольник" or figure == "прямоугольный равносторонний треугольник":
                    side = int(input("Введите сторону треугольника: "))
                    print("Периметр равен: ", (side*2 + side**0.5))
                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                elif figure == "треугольник":
                    side = int(input("Введите известную сторону треугольника: "))
                    degreesAngle = int(input("Введите косинус угла между известными сторонами: "))
                    radiansAngle = math.radians(degreesAngle)
                    angleCos = math.cos(radiansAngle)
                    print("Периметр равен: ", (side*2 + side**2 + side**2 - 2*2*side * angleCos))
                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                elif figure == "прямоугольник":
                    lenght = int(input("Введите длину прямоугольник: "))
                    width = int(input("Введите ширину прямоугольника: "))
                    print("Периметр равен: ", (lenght + width) * 2)
                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                elif figure == "круг":
                    print("Что вам известно?\nЕсли ничего, то поставьте 0: ")

                    diametr = int(input("Диаметр: "))
                    radius = int(input("Радиус: "))
                    if diametr == 0 and radius == 0: 
                        print("Я не могу найти с такими значениями. ")
                    elif diametr ==0 and radius != 0:
                         print(f"Результат: 2 * 3.14 * {radius} = {2 * 3.14 * radius}")
                    elif diametr != 0 and radius == 0:
                         print(f"Результат: 3.14 * {diametr} = {3.14 * diametr} ")
                    else: 
                         print(f"\n\nЕсть два способа нахождения через диаметр и через радиус")
                         print(f"Периметр = p * Диаметр ({3.14*diametr})")
                         print(f"Периметр = 2 * 3.14 * Радиус ({2*3.14*radius})")
                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                else:
                     print("Такой пока фигуры нет.")
                     continue
        elif action == "площадь":
                if figure == "квадрат":
                    side = int(input("Введите сторону квадрата: "))
                    print(f"Площадь равна: {side**2}")

                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                elif figure == "прямоугольник":
                    lenght = int(input("Введите длину прямоугольника: "))
                    width = int(input("Введите ширину прямоугольника: "))
                    print("Площадь равна: ", lenght * width)
                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                    if tape == 1:
                         continue
                    elif tape == 0:
                         break
                elif figure == "круг":
                    print("Что вам известно?\nЕсли ничего, то поставьте 0: ")

                    diametr = int(input("Диаметр: "))
                    radius = int(input("Радиус: "))
                    if diametr == 0 and radius == 0: 
                        print("Я не могу найти с такими значениями. ")
                    elif diametr ==0 and radius != 0:
                         print(f"Результат: 3.14 * {radius} ** 2 = {3.14 * (radius ** 2)}")
                    elif diametr != 0 and radius == 0:
                         print(f"Результат: (3.14 * {diametr}**2)/4 = {(3.14 * (diametr ** 2))/4} ")
                    else: 
                         print(f"\n\nЕсть два способа нахождения через диаметр и через радиус")
                         print(f"Площадь = (p * (Диаметр ** 2))/4 ({(3.14 * (diametr ** 2))/4})")
                         print(f"Площадь = 3.14 * (Радиус ** 2) ({3.14 * (radius ** 2)})")
                    tape = int(input("Если хотите продолжить, то введите 1, если хотите закончить введите 0: "))
                else:
                     print("Такой пока фигуры нет.")
                     continue
        else:
                     print("Такого действия пока нет.")
                     continue
except SyntaxError:
    print("Произошла непредвиденная ошибка, вы ни в чем не виноваты. разработчик скоро исправит. ")
