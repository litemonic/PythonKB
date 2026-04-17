import json
from functools import wraps

def authorize(func):
    @wraps(func)
    def wrapper(current_user, *args, **kwargs):
        if current_user.get("role") == "admin":
            return func(current_user, *args, **kwargs)
        else:
            print(f"Доступ запрещён для пользователя {current_user.get('name')}")
            print("Требуются права администратора")
            return None
    return wrapper

def load_user():
    try:
        with open("users.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data.get("user", [])
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка чтения файла")
        return []

def save_user(user):
    try:
        with open("users.json", 'r', encoding="utf-8") as file:
            json.dump({"user":user}, file, ensure_ascii=False, indent=4)
        print("Данные успешно сохранены")
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

@authorize    
def users_show():
    users = load_user()
    if not users:
        print("пользователя нет в системе")
        return
    print(f"Список пользователей (всего: {len(users)}")

    for i, user in enumerate(users, 1):
        role_icon = "-__- "if users.get("role") == "admin" else "_--_"
        print(f"пользователь {i} {role_icon} {user('name')} - роль: {user("role")} (пароль: {user("password")})")

    print("\n")

@authorize
def add_user(current_user):
    print("\nДобавление нового пользователя\n")
    name = input("Введите имя пользователя: ").strip()
    if not name:
        print("Имя не может быть пустым. ")
        return
    password = input("Введите пароль: ").strip()
    if not password:
        print("Пароль не может быть пустым. ")
        return
    role = input("Введите роль: ").strip()
    if role not in ["admin", "user"]:
        print("Роль должна быть 'admin' или 'user' ")
        return

    users = load_user()

    for user in users:
        if user["name"].lower() == name.lower():
            print(f"Пользователь с именем {name} существует. ")
            return

    new_user = {"name": name,
                "role": role,
                "password":password

    }    
    users.append(new_user)

    if save_user(new_user):
        print(f"Пользователь '{name}' успешно добавлен. ")
        return

def admin_menu(current_user):
    while True:
        print("Это админ меню, у вас в арсенале: ")
        print("1. Посмотреть всех пользователей")
        print("2. Добавить пользователей")
        print("3. Удалить пользователей")
        print("4. Выход из системы")

        choice = input("Выберите действие (1,2,3,4)")

        if choice == "1":
            users_show(current_user)
        elif choice == "2":
            add_user(current_user)
        elif choice == "3":
            print("в разработке")
        elif choice == "4":
            print("До встречи.")
            return False
        else:
            print("Неверный выбор")
    return True

def main():
    print("Система управления пользователями")
    while True:
        current_user = load_user
        if current_user:
            if current_user["role"] == "admin":
                admin_menu(current_user)
                break
            else:
                print("Вы вошли как обычный пользователь, у вас нет прав доступа.")
        else:
            retry = input("Попробовать снова?")
            if retry != "да":
                print("Завершение программы")
                break

if __name__ == "__main__":
    main()