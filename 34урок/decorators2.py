'''def decorator1(func):
    def wrapper():
        print("Декоратор 1")
        func
    return wrapper

def decorator2(func):
    def wrapper():
        print("Декоратор 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Привет!")
say_hello()'''
'''def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a,b):
    return a + b

print(add(3,4))'''
#------------------------------------------------------------------------------
def authorize(func):
    def wrapper(user):
        if user == "admin":
            return func()
        else:
            print("Доступ запрещён")
        return wrapper
    
@authorize
def secret():
    print("Секретная информация")

secret("admin")
secret("guest")
#----------------------------------------------------------------------------