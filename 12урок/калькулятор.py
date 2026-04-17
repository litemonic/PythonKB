'''Прошаренный калькулятор'''
import math
while True:
    try:
        num1 = float(input("Введите число: "))
        print("Прошаренный калькулятор")
        print("""
У вас есть выбор следующих действий:
 + (сложение)
 - (вычитание)
 * (умножение)
 / (деление)
 ^ (возведение в степень)
 & (нахождение квадратного корня числа)
 ! (нахождение факториала)
        """)
        action = input("Выберите одно из предложенных действий")
        match action:
            case "+":
                num2 = float(input("Введите второе число: "))
                result = num1 + num2
            case "-":
                num2 = float(input("Введите второе число: "))
                result = num1 - num2
            case "*":
                num2 = float(input("Введите второе число: "))
                result = num1 * num2
            case "/":
                num2 = float(input("Введите второе число: "))
                if num2 == 0:
                    print("На ноль делить нельзя")
                else:
                    result = num1 / num2
            case "^":
                num2 = float(input("Введите степень в которую хотите возвести: "))
                result = num1 ** num2
            case "&":
                result = math.sqrt(num1)
            case "!":
                result = 1
                for i in range (1, int(num1)):
                    result *= i
            case _:
                print("Неизвестная операция")
                continue
        match action:
            case "&":
                print(f"Квадратный корень: {result:.2f}")
            case "!":
                print(f"Факториал: {result}")
            case _:
                print(f"Результат: {result}")
    except ValueError:
        print("Вводите числа!!! ")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    again = input("Желаете продолжить? (да/нет): ").strip().lower()
    if again != "да":
        print("До свидания!")
        break
    else:
        continue