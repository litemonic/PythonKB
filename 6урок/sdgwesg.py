'''
Аналог структуры if elif else:
match - данные
case - условие

color = input("Выберите цвет: ")
year = int(input("Введите ваш возвраст: "))
name = input("Введите своё имя: ")
match color:
    case "красный":
        print("Вы выбрали красный")
    case "черный":
        print("Вы выбьрали черный")
    case "белый":
        print("Вы выбрали белый")
    case "синий":
        if year == 6:
            print("Вы выбрали синий")
        else:
            match name:
                case "Admin":
                    password = int(input("Введите пароль: "))
                    if password == 123:
                        print("Welcome")
    case _:
        print("такого цвета нет.")
'''

num1 = int(input("Введите первую сторону треугольника: "))
num2 = int(input("Введите вторую сторону треугольника: "))
num3 = int(input("Введите третью сторону треугольника: "))

match True:
    case True if num1 + num2 > num3:
        print("Да, такой треугольник есть.")
    case True if num1 + num3 > num2:
        print("Да, такой треугольник есть.")
    case True if num3 + num2 > num1:
        print("Да, такой треугольник есть.")
    case _:
        print("Такого быть не может.")
