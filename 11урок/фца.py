while True:
    try:
        sumOfMarks = 0
        numOfMarks = int(input("Введите количество оценок"))
        if numOfMarks < 2:
            print("Это не имеет смысла, чисел нужно как минимум два")
        else:
            for i in range(numOfMarks):
                sumOfMarks += float(input("Введите оценку"))
        print(f"Среднее арифметическое равно: {sumOfMarks/numOfMarks}")
        action = input("Хотите продолжить? (да/нет): ").lower()
        match action:
            case "да":
                print("Программа продолжает роботу.")
                continue
            case "нет":
                print("Программа заканчивает работу")
                break
            case _:
                print("Напишите 'да' или 'нет'")
                continue
    except ValueError:
        print("\n!!! Вы ввели не число, а нужно конкретное число\n")


