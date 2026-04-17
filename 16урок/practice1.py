userGenre = {}
try:
    while True:
        userInput = int(input("Введите команду: \n"
        "1.Вывести список жанров.\n"
        "2.Добавить жанр.\n"
        "3.Удалить жанр.\n"
        "4.Закрыть программу."))
        if userInput == 1:
            for genre, yearAndDescr in userGenre.items():
                print(f"{genre} : {yearAndDescr}")
        elif userInput == 2:
            genre = input("Введите название жанра: ")
            year = input("Введите год в котором вам понравился жанр: ")
            descr = input("Введите описание жанра: ")
            userGenre[genre] = {year, descr}
            #.setdefault в данном случае менее экономно
        elif userInput == 3:
            delInfo = input("Введите название жанра, который хотите удалить: ")
            del userGenre[delInfo]
        elif userInput == 4:
            break
except Exception as e:
    print(f"Ошибка: {e}")
#Exception это все ошибки
#TypeError это ошибки смешивания типов