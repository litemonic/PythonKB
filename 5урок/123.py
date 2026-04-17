userInput = int(input("Введите число: "))
num = 1

for i in range(userInput):
    print(f"Число: {num}")
    num += 1
    if num == 5:
        print("Пасхалка")
        continue
    if num > 10:
        print("Работа закончена из-за ограничений.")
        break