txt = input("Введите текст: ")
mf = open("file.txt", "w+t")

a = 1
mf.write(txt)
mf.seek(0)

print(mf.tell(), "->", mf.read(1))

mf.seek(0, 2)

num = mf.tell() -1
mf.seek(num)

print(mf.tell(), "->", mf.read(1))
mf.seek(0)

print("Три первых символа", mf.read(3))

mf.close
print("\nФайл закрыт")