numOfFactorial = int(input("Введите число, факториал которого хотите найти: "))
factorial = 1
if numOfFactorial == 0:
    print(1)
else:
    for i in range(2, numOfFactorial + 1):
        factorial *= i
print(factorial)
