print("У нас такое уравнение: Ax = B - A - 1")
numA = int(input("Введите значение A: "))
numB = int(input("Введите значение B: "))

match True:
    case True if numA == 0:
        if numB == 1:
            print("решение это любое число")
        elif numB != 1:
            print("решений нет")
    case _:
        print("error")
'''
if numA == 0:
    if numB == 1:
        print("Решением является любое число")
    elif numB != 1:
        print("Решений нет.")
'''