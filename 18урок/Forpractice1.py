chet = 1
start = 1
num = int(input("Таблицу умножения какого числа вы хотите видеть: "))
score = int(input("Сколько чисел хотите видеть: "))
question = int(input("Какие значения хотите видеть: " \
"1 - все" \
"2 - только четные" \
"3 - только НЕ четные"))

if question == 1:
    pass
elif question == 2:
    chet = 2
elif question == 3:
    chet = 2

for i in range (start, score + 1, chet):
    print(f"{num} * {i} = {num * i}")