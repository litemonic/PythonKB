def calculate(num1, num2, operation = "+"):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка. Делить на ноль нельзя"
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation = input("Введите операцию, которую хотите совершить: ")
if operation:
    print(calculate(num1, num2, operation))
else:
    print(calculate(num1, num2))