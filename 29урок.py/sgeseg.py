userInput = int(input("Шестизначное число: "))
def HappyTicket(a):
    res1 = 0
    res2 = 0
    spisik = str(a)
    for i in range(len(spisik)):
        if 0 <= i <= 2:
            res1 += int(spisik[i])
        elif 3 <= i <= 5:
            res2 += int(spisik[i])
    if res1 == res2:
        print("билет счастливый")
    else:
        print("билет не счастливый")
HappyTicket(userInput)