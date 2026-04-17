def smth(x):
    return x ** 2
def main(res, a = -5, b = 5):
    if res > a and b < res:
        return res
    else:
        return None
x = int(input("Введите число для возведения в квадрат"))
print(main(smth(x), -5, 5))
