import re

def check_login(login):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{3,16}$"
    if re.match(pattern, login):
        return True, "Логин подходит"
    else:
        if len(login) < 4:
            return False, "Логин слишком короткий"
        if len(login) > 16:
            return False, "Логин слишком большой"
        if login[0].isdigit():
            return False, "Логин не может начинаться с цифры"
        if not re.match(pattern, login):
            return False, "Логин содержит недопустимые символы"
        return False, "Логин не соответствует правилам написания"
    
def password_check(password):
    if len(password) < 6:
        return False, "Пароль слишком короткий"
    if not re.search(r"\d", password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    if not re.search(r"[a-z]", password):
        return False, "Пароль должен содержать хотя бы одну маленькую букву"
    if not re.search(r"[A-Z]", password):
        return False, "Пароль должен содержать хотя бы одну большую букву"
    else:
        return True, "Пароль надежный."

print("Регистрация нового пользователя") 

print("\nТребования к логину: ")
print("""- только буквы, цифры и спецсимвол _
- длина от 4 до 16 символов
- не может начинаться с цифры
""")
while True:
    login = input("\nВведите желаемый логин: ")
    isValid, message = check_login(login)

    print(f"    {message} ")
    if isValid:
        break
    else:
        print("Попробуйте ещё раз")
print("\nТребования к паролю: ")
print("""- хотя бы одна маленькая буква
- хотя бы одна цифра
- хотя бы одна большая буква
""")
while True:
    password = input("\nВведите желаемый пароль: ")
    isValid, message = password_check(password)

    print(f"    {message} ")
    if isValid:
        confirm = input("Повторите пароль: ")
        if password == confirm:
            print("Регистрация прошла успешно")
            print(f"Добро пожаловать, {login}")
        else:
            print("Попробуйте ещё раз")
    else:
        print("Попробуйте ещё раз")

