filename = input("Введите название файла: ")
userInput = input("Введите текст в файл: ").lower()

with("filename", "w", "utf-8") as file:
    file.write(userInput)
    file.read
