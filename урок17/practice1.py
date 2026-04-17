'''

'''
bools = True
spisik = []
x = 0
score = int(input("сколько фильмов вы хотите ввести?: "))
if score < 0:
    bools = False
while bools:
    while x < score:
        inputFilm = input("Введите название фильма: ").strip()
        spisik.append(inputFilm)
        x += 1
        if x == 9:
            break
    break
print(spisik)