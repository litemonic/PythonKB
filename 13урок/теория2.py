'''
списки между собой можно складывать
sorted - сортировка списка по возврастанию
copy - независимая копия списка для работы('a' не изменяется если
например изменять b = a при а = [1,2,3...])

'''


spisik = int(input("Введите количество чисел: "))
osnSpisik = []
for i in range(spisik):
    element = int(input("Введите элемент списка: "))
    if 1 <= element <= 12:
        osnSpisik.append(element)
    else:
        print("Данное число не является оценкой")


num = len(osnSpisik)
if num == spisik:
    print(f"среднее арифметическое: {sum(osnSpisik) / spisik}")
else:
    print(f"Оценок было принято прграммой: {num}")
    print(f"среднее арифметическое: {sum(osnSpisik) / num}")
