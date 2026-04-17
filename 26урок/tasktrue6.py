def report(func, a):
    for _ in range(a):
        summa = func(x)
    return summa
    

def double(x):
    return x**2
y = int(input("число повторений: "))
x = int(input("главное число: "))
doubleItm = report(double, y)
print(doubleItm)