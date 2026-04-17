def filter_and_square(numbers, trashhold):
    for i in numbers:
        if numbers[i]**2 < trashhold:
            yield numbers[i]**2

userInput = int(input("Введите числа через пробел для списка: "))
trashhold = int(input("Введите число-ограничение: "))
spisik = []
for i in range(len(userInput)):
    spisik.append(userInput[i])
print(filter_and_square(spisik, trashhold))