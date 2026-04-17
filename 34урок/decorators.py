'''def decorator(func):
    def wrapper():
        print("До вызова функции")
        func
        print("После вызова функции")
    return wrapper

@decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Иван")
'''
'''class MyClass:
    @staticmethod
    def greet():
        print("Привет из статического метода!")

MyClass.greet()'''

class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count