k = 1
filename = input("Введите название файла: ")
with(filename, "r", "utf-8") as file:
    print(file.read())
with(filename, "w", "utf-8") as file:
    print("Построчное считывание файла: ")
    i = file.readline()

    while i != "":
        print(f"[{str(k)}]", i, end="")
        k+=1
        i = file.readline()
