userInput = int(input("Введите количество степеней двойки: "))
spisik = list()
for i in range(0, userInput + 1):
    spisik.append(2**i)
print(spisik)