userInput = int(input("Введите число: "))
userInputStr = str(abs(userInput))

transformer = {
    '0' : '9',
    '1' : '8',
    '2' : '7',
    '3' : '6',
    '4' : '5',
    '5' : '4',
    '6' : '3',
    '7' : '2',
    '8' : '1',
    '9' : '0'
}

resultatStr = ''.join(transformer[dict] for dict in userInputStr)
if userInput < 0:
    resultatStr = '-' + resultatStr
print(resultatStr)