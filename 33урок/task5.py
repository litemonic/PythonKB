userInput = int(input("Введите числа через пробел: ").strip()) #нельзя так делать!!!!
spisik = []
for i in range(len(userInput)):
    spisik.append(userInput[i])
iterated_nums = iter(spisik)
res = 0
while True:
    try:
        step = next(iterated_nums)
        print(step)
        res += step
    except StopIteration:
        print(f"список закончился, сумма равна: {res}")
        break