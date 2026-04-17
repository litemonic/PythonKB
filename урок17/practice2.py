numAmount = int(input("Введите количество чисел: "))
x = 0
nums = set()
try:
    while x < numAmount:
        numInput = int(input("Введите число: "))
        nums.add(numInput)
        x += 1
    for num in nums:
        print(f"{num}")
except TypeError as e:
    print(f"Ошибка: {e}")