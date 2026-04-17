num = int(input("Введите число: "))

n = abs(num)

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print(f"В числе {n} содержится {count} символов.")