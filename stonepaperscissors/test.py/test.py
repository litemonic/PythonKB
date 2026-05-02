import random
print("Вы запустили игру 'Камень, ножницы, бумага'.")
rounds = int(input("Введите количество раундов, которые хотите сыграть: "))
#1 - камень, 2 - ножницы, 3 - бумага
countOfRound = 1
roundsOfPlayer = 0
roundsOfBot = 0
while countOfRound <= rounds:
    playerAction = int(input("Введите свой выбор(камень - 1, ножницы - 2, бумага - 3): "))
    actionOfBot = random.randint(1, 3)
    if playerAction == actionOfBot:
        print(f"Ничья, Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
    if playerAction == 1:
        if actionOfBot == 2:
            print("Компьютер выбрал ножницы")
            roundsOfPlayer += 1
            print(f"Камень бьёт ножницы. Игрок победил! Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
        elif actionOfBot == 3:
            print("Компьютер выбрал бумагу")
            roundsOfBot +=1
            print(f"Бумага обворачивает камень. Компьютер победил! Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
    if playerAction == 2:
        if actionOfBot == 1:
            print("Компьютер выбрал камень")
            roundsOfBot += 1
            print(f"Камень бьёт ножницы. Компьютер победил! Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
        elif actionOfBot == 3:
            print("Компьютер выбрал бумагу")
            roundsOfPlayer += 1
            print(f"Ножницы режут бумагу. Игрок победил! Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
    if playerAction == 3:
        if actionOfBot == 1:
            print("Компьютер выбрал камень")
            roundsOfPlayer +=1
            print(f"Бумага обворачивает камень. Игрок победил! Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
        elif actionOfBot == 2:
            print("Компьютер выбрал ножницы")
            roundsOfBot +=1
            print(f"Ножницы режут бумагу. Компьютер победил! Счёт: Игрок - {roundsOfPlayer}, Компьютер - {roundsOfBot}")
    countOfRound += 1

if roundsOfPlayer == roundsOfBot:
    print("По истечении раундов объявлена НИЧЬЯ!")
if roundsOfBot > roundsOfPlayer:
    print(f"По истечении раундов победил Компьютер со счётом: {roundsOfBot}")
if roundsOfPlayer > roundsOfBot:
    print(f"По истечении раундов победил Игрок со счётом: {roundsOfPlayer}")