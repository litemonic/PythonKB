print("===Проверка чисел===")

while True:
    try:
        num = int(input("Введите число: "))

        if num > 0:
            print("Число положительное. ")
        elif num > 0:
            print("Число отрицательное. ")
        else:
            print("Ноль")
    except ValueError:
        print("Ошибка, введи число!")
    
    prodolzh = input("Хотите продолжить? ").lower()
    match prodolzh:
        case "да" | "yes" | 'д':
            print("Продолжаем...\n")
        case "нет" | "no" | "н":
            print("Завершение программы\n")
            break
        case _:
            print("Неизвестная команда. Пока")
            break
