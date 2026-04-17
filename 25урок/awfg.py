'''
r = read
w = write
a = append
x = exclusive
b = binary
+ = чтение и запись
'''
print("Начинаем копирование файла")

try:
    A = open("file.txt", "rb")
    B = open("Снимок экрана.jpg", "xb")

    B.write(A.read())

    A.close()
    B.close()
except FileExistsError:
    print("Файл уже есть")
except: 
    print("Ошибка доступа к файлу")
print("Программа выполнила работу.")