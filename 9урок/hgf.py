userAge = int(input("Введите свой возвраст: "))
selery = int(input("Введите свой доход: "))
sumOfMoney = int(input("Введите количество денег в сбережениях: "))
riskProfile = int(input("Введите свой риск-профиль(1 - низкий, 2 - средний, 3 - высокий: )"))

if userAge < 18:
    print("Сосредоточтесь на учебе, о деньгах побеспокоитесь потом.")
elif 18 < userAge < 25:
    if selery < 30000:
        print("Советуем накопить подушку безопасности.")
    elif selery >= 30000 and sumOfMoney > 100000:
        print("попробйте облигации.")
    elif selery >= 30000 and sumOfMoney < 100000:
        print("попробуйте накопить денег.")
elif 26 < userAge <= 60:
    if riskProfile == 1:
        print("рассмотрите вклады.")
    elif riskProfile == 2:
        if sumOfMoney > 500000:
            print("50% в акции, 50% - можете тратить.")
        else:
            print("рассмотрите облегации.")
    elif riskProfile == 3:
        if sumOfMoney > 100000:
            print("используйте акции роста.")
        else:
            print("высокий риск не порадан, ничего не делайте")
elif 150 > userAge > 60:
    print("основная цель экономить и накопить денег.")
else:
    print("вы что-то ввели не так, можете попробовать ещё раз?")