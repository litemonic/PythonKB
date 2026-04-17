from trigonometry import formuls
from trigonometry import fact
from show import sin
from show import cos
from show import tg
from show import ctg
from pril import formater
from pril import loger
print("""
Данная программа может находить:
1.sin
2.cos
3.tg
4.ctg

""")

def main():
    choice = input("Что хотите найти? ").lower()

    try:
        if choice == "sin":
            print("Чтобы найти sin нам потребуется узнать следующее: ")
            num1 = int(input("Введите длину катета треугольника: "))
            num2 = int(input("Введите длину гипотенузы треугольника: "))
            res = formuls.sin(num1, num2)
            print(formater.formatResult(choice, res))

            print("Для визуализации мы должны понять длину третьей стороны: ")
            num3 = int(input("Введите длину второго катета треугольника: "))
            res2 = fact.check(num1,num2,num3)

            if res2 == True:
                print("приступим к визулизации")
                sin.ShowSin(num1, num3, res)
            else:
                print("Приступить к визуализации не можем, треугольника не существует")
        elif choice == "cos":
            print("Чтобы найти cos нам потребуется узнать следующее: ")
            num1 = int(input("Введите длину катета треугольника: "))
            num2 = int(input("Введите длину гипотенузы треугольника: "))
            res = formuls.cos(num1, num2)
            print(formater.formatResult(choice, res))

            print("Для визуализации мы должны понять длину третьей стороны: ")
            num3 = int(input("Введите длину второго катета треугольника"))
            res2 = fact.check(num1,num2,num3)

            if res2 == True:
                print("приступим к визулизации")
                cos.ShowCos(num2, num3, res)
            else:
                print("Приступить к визуализации не можем, треугольника не существует")
        elif choice == "tg":
            print("Чтобы найти tg нам потребуется узнать следующее: ")
            num1 = int(input("Введите длину первого катета треугольника: "))
            num2 = int(input("Введите длину второго катета треугольника: "))
            res = formuls.tg(num1, num2)
            print(formater.formatResult(choice, res))

            print("Для визуализации мы должны понять длину третьей стороны" )
            num3 = int(input("Введите длину гипотенузы треугольника: "))
            res2 = fact.check(num1,num2,num3)

            if res2 == True:
                print("приступим к визулизации")
                tg.ShowTg(num1, num2, res)
            else:
                print("Приступить к визуализации не можем, треугольника не существует")
        elif choice == "ctg":
            print("Чтобы найти сtg нам потребуется узнать следующее: ")
            num1 = int(input("Введите длину первого катета треугольника: "))
            num2 = int(input("Введите длину второго катета треугольника: "))
            res = formuls.ctg(num1, num2)
            print(formater.formatResult(choice, res))

            print("Для визуализации мы должны понять длину третьей стороны")
            num3 = int(input("Введите длину гипотенузы треугольника: "))
            res2 = fact.check(num1,num2,num3)

            if res2 == True:
                print("приступим к визулизации")
                ctg.ShowCtg(num2,num1,res)
            else:
                print("Приступить к визуализации не можем, треугольника не существует")
        else:
            print(f"Error! операция {choice} невозможна")

    except Exception as e:
        loger.errorInfo(e)
if __name__ == "__main__":
    main()