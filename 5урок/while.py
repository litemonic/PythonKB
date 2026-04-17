print("=" * 30)
print(" " * 8, "Калькулятор")
print("=" * 30)

while True:
    num1 = int(input("\nВведите первое число: "))
    num2 = int(input("Введите второе число: "))

    operation = input("Выберите действие для работы(+,-,*,/): ")
    if operation == "+":
        print(f"Результат: {num1 + num2}")
        a = int(input("Хотите продолжить?(введите 1 если хотите)"))
        if a == 1:
            continue
        else:
            print("Конец.")
            break
    elif operation == "-":
        print(f"Результат: {num1 - num2}")
        a = int(input("Хотите продолжить?(введите 1 если хотите)"))
        if a == 1:
            continue
        else:
            print("Конец.")
            break
    elif operation == "*":
        print(f"Результат: {num1 * num2}")
        a = int(input("Хотите продолжить?(введите 1 если хотите)"))
        if a == 1:
            continue
        else:
            print("Конец.")
            break
    elif operation == "/":
        if num2 == 0:
            print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!")
            continue
        else:
            print(f"Результат: {num1 / num2}")
            a = int(input("Хотите продолжить?(введите 1 если хотите)"))
            if a == 1:
                continue
            else:
                print("Конец.")
                break
