spisik = int(input("Введите количество цен: "))
osnSpisik = []
rest = int(input("Какой ценник будет считаться дорогим: "))
for i in range(spisik):
    element = int(input("Введите цену: "))
    if element > 0:
        osnSpisik.append(element)
        print("Ценник на товар добавлен")
    else:
        print("Данное число не является ценой")
print(f"Самая дорогая покупка: {max(osnSpisik)}")
print(f"Самая дешёвая покупка: {min(osnSpisik)}")
print(f"средняя цена товара: {sum(osnSpisik) / len(osnSpisik)}")
print(f"Ваш список в сортированном виде: {sorted(osnSpisik)}")
