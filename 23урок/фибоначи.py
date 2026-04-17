def fibanachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    listik = list()
    for _ in range(n):
        a, b = b, a + b
        listik.append(b)
    return listik
n = int(input("Введите количество чисел фибоначи:"))
print(f"F({n}) = {fibanachi(n)}")