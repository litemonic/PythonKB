def order(a,b):
    spisik = ""
    for i in b:
        if 0 <= i < len(a):
            spisik += a[i]
    return spisik
a = "Программирование"
b = [1,2,6,4,0]
print(order(a,b))