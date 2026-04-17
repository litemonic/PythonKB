'''
"D:\\Books\\Python\\txt.txt"
'''
mf = open('цпуп.txt')
k = 1
print("Построчное считывание файла: ")
i = mf.readline()

while i != "":
    print(f"[{str(k)}]", i, end="")
    for j in i:
        if j == " ":
            j = "+"
        print(j, end="")
    k+=1
    i = mf.readline()
mf.close
print("файл закрыт")