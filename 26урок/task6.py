def binar(a):
    binarA = bin(a)[2:]
    res = sum(binarA)
    return res
num = int(input("Введите число: "))
print(num)
print(binar(num))
