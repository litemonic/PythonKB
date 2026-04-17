from functools import wraps

def authorize_admin(func):
    wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") == "admin":
            return func(user, *args, **kwargs)
        else:
            print(f"Доступ запрещён для пользователя: {user.get('name')}")
    return wrapper

@authorize_admin
def view_secret_data(user):
    print(f"Секретные данные доступны для: {user.get('name')}")

admin_user = {
    "name": "Vlad",
    "role":"admin"
}

user = {
    "name":"Oleg",
    "role":"user"
}
view_secret_data(admin_user)
view_secret_data(user)