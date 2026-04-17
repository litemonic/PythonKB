inHome = {"apple","banana","orange","mango","kiwi","pear"}
wantToBuy = set()
while True:
    userinput = (input("Введите продукты, которые хотите купить(чтобы завершить, " \
    "введите цифру 1.): "))
    if userinput == '1':
        break
    else:
        wantToBuy.add(userinput)
    
print(f"Товары, которые уже есть дома: {inHome & wantToBuy}")
print(f"Товары, которые нужно купить: {wantToBuy - inHome}")