class Book:
    def __init__(self, title, author, status="В наличии"):
        self.title = title
        self.author = author
        self.status = status
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def change_status(self, title, new_status):
        for book in self.books:
            if book.title == title:
                book.status = new_status
                return f"Статус книги '{title}' изменен на '{new_status}'"
        return f"книга '{title}' не найдена"
    def show_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
        else:
            print("список книг в библиотеке: ")
            for book in self.books:
                print(f"{book.title} ({book.author}) - {book.status}")

library = Library()

while True:
    command = input("Введите команду (add, change, show, exit)")
    match command:
        case "add":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            library.add_book(Book(title, author))
        case "change":
            title = input("Введите название книги: ")
            new_status = input("Введите новый статус для книги: ")
            print(library.change_status(title, new_status))
        case "show":
            print("Список книг: ")
            library.show_books()
        case "exit":
            print("Программа завершена.")
            break
        case _:
            print("Неизвестная команда. ")