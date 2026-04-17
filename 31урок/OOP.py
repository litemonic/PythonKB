"""class MyClass:
    pass

A = MyClass()
B = MyClass()

print("первый объект", A)
print("второй объект", B)
print(f"сравнение {A == B}")

print("Класс А:", type(A).__name__)
print("Класс В:", type(B).__name__)

self - ссылка на объект

"""
"""class MyClass:
    def set(self, n):
        self.number = n
    
    def show(self):
        print(f"Поле number = {self.number}")

"""
"""Конструктор - __init__

class Car:
    wheels = 4 #атрибут класса
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
my_car = Car("Toyota", "красный")
friend_car = Car("Ford", "синий")"""
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0
class Classroom:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def add_grade_to_student(self, name, grade):
        for student in self.students:
            if self.student.name == name:
                student.add_grade(grade)
                return f"Оценка {grade} добавлена дял {name}"
        return f"Ученик с именем {name} не найден"
    def show_students(self):
        if not self.students:
            print("Список учеников пуст. ")
        else:
            for student in self.students:
                print(f"{student.name} - средний балл {student.average_grade():.2f}")
classroom = Classroom()

while True:
    command = input("Введите команду(1 - добавить студента, 2 - добавить оценку, 3 - показать, 4 - выйти)")
    match command:
        case "1":
            name = input("Введите имя ученика: ").strip()
            classroom.add_student(Student(name))
            print(f"Ученик {name} добавлен.")
        case "2":
            name = input("Введите имя ученика: ").strip()
            grade = input("Введите оценку: ")
            print(classroom.add_grade_to_student(name, grade))
        case "3":
            classroom.show_students()
        case "4":
            print("Программа завершена. ")
            break
        case _:
            print("Введите команду из списка. ")

