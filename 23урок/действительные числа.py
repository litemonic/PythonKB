num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
try:
    print(num1 if num1 > num2 else num2)
except Exception as e:
    print(f"error: {e}")