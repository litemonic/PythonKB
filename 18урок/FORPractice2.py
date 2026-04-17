guests = []
f = 0
while True:
    num = int(input("Сколько гостей вы хотите видеть: "))

    for i in range(1, num + 1):
        guest = input("Введите имя гостя")
        guests.append(guest)

    print("На данный момент следующие гости: ")
    for guest in guests:
        print(f"Гость{f}: {guest}")
        f += 1
    f = 0
    choose = input("Хотите продолжить? ").strip().lower()
    if choose == "да" or "yes" or "y" or "д":
        pass
    elif choose == "нет" or "no" or "n" or "н":
        break
    else:
        break