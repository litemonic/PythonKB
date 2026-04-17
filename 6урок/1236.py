'''
positiveNum = 0
while True: 
    num = int(input("Вводите числа (если хотите остановится, нажмите 0)"))
    match num:
        case pos if num > 0:
            positiveNum += num
        case 0:
            break
print(f"Сумма положительных чисел равна: {positiveNum}.")
'''
positiveNum = 0
while True:
    num = int(input("Вводите числа (если хотите остановится, нажмите 0: "))
    if num > 0:
        positiveNum += num
    elif num < 0:
        print("Вводите положительные числа.")
        continue
    elif num == 0:
        break
print(f"Сумма положительных чисел равна: {positiveNum}. ")