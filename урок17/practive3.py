print("Пишите числа, если надоест пишите 0")
multipleBy2 = set()
multipleBy3 = set()
multipleBy4 = set()
multipleBy5 = set()
nums = {
    "by2":multipleBy2,
    "by3":multipleBy3,
    "by4":multipleBy4,
    "by5":multipleBy5
}
listik = list()
try:
    while True:
        userInput = int(input("Введите число: "))
        
        if userInput == 0:
            print(nums)
            print()
            break
        elif userInput % 2 == 0:
            if userInput % 4 == 0:
                multipleBy4.add(userInput)
            else:
                multipleBy2.add(userInput)
        elif userInput % 3 == 0:
            if userInput % 5 == 0:
                multipleBy5.add(userInput)
            else: 
                multipleBy3.add(userInput)
except Exception as e:
    print(f"Ошибка: {e}")
            