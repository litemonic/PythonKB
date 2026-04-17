matrix = [[11,12,13],
          [21,22,23],
          [31,32,33]]

print ("Матрица А: ")
for index, item in enumerate(matrix,1):
    print(f"Строка: {index} = {item}")

a = input("Введите выражение: ")
f = eval(a)