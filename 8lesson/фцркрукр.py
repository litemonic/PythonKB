print("Вы открыли программу под названием КОНВЕРТАТОР.\n")
print("она конвертирует см в мм, см в м, см в км")

while True:
    try:
        numCm = float(input("\nВведите число в сантиметрах: "))
        print("""Выберите действие:
        1. перевести ваше число в милиметры
        2. перевести ваше число в метры
        3. перевести ваше число в км 
        4. все варианты
        5. выход
        """)
        operation = int(input("Введите действие(1,2,3,4,5): "))
        if operation == 1:
            print(f"Ваши {numCm} см переведены в {numCm * 10} мм.")
            continue
        elif operation == 2:
            print(f"Ваши {numCm} см переведены в {numCm / 100} м.")
            continue
        elif operation == 3:
            print(f"Ваши {numCm} см переведены в {numCm / 1000000} км.")
            continue
        elif operation == 4:
            print(f"Ваши {numCm} см переведены в {numCm * 10} мм.")
            print(f"Ваши {numCm} см переведены в {numCm / 100} м.")
            print(f"Ваши {numCm} см переведены в {numCm / 1000000} км.")
            continue
        elif operation == 5:
            break
    except ValueError:
        print("Пожалуйста, введите число")
    except SyntaxError:
        print("Косяк разраба. ")
print("пока")
