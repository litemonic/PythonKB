'''
a = 1 # int/integer - целые числа
b = "Slovo" # str/string
c = 1.5 # float - числа с плавающей точкой
d = True # bool, логический тип данных
e = False # bool/boolive

userTxt = input("Напишите ваше имя") # str
userNum = int(input("Напишите ваш возвраст")) # int
userPool = float(input("Напишите ваш средний балл")) #float


print("Программа, которая переводит рубли в другую валюту")

rub = int(input("Введите значение в рублях: "))
action = input("Выберите валюту(usd, eur, un)")

if action == "usd":
    print(f"В {rub} рублях {rub/80} долларов.")
elif action == "eur":
    print(f"В {rub} рублях {rub/100} евро.")
elif action == "un":
    print(f"В {rub} рублях {rub/20} юаней.")
else:
    print("Некорректный ввод данных, введите что-то из списка(usd, eur, un)")
'''

print('=' * 30)
print("Программа по нахождению пермитра и площади геометрических фигур.")
print('=' * 30)
operation = input("Выберите операцию, которую необходимо совершить(Периметр, Площадь)")
figure = input("Выберите фигуру, с которой вы хотите работать(прямоугольный треугольник, треугольник, квадрат, прямоугольник)")
length = int(input("Введите длину фигуры: "))
if figure == "треугольник":
    width = int(input("Введите высоту фигуры: "))
else:
    width = int(input("Введите ширину фигуры: "))


if figure == "прямоугольный треугольник":
    if operation == "площадь":
        print(f"Результат: {length * width / 2}")
    elif operation == "периметр":
        print(f"Результат: {length + width + ((length**2 + width**2)**0.5)} ")
elif figure == "квадрат":
    if operation == "площадь":
        print(f"Результат: {length*width}")
    elif operation == "периметр":
        print(f"Результат: {(length+width)*2}")
elif figure == "прямоугольник":
    if operation == "площадь":
        print(f"Результат: {length*width}")
    elif operation == "периметр":
        print(f"Результат: {(length+width)*2}")
elif figure == "треугольник":
    if operation == "площадь":
        print(f"Результат: {length * width / 2}")
    elif operation == "периметр":
        print(f"Результат: {length + width + ((length**2 + width**2)**0.5)} ")
else:
    print("такой фигуры нет.")
