from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        with open("actions.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"Пользователь: {username}, действие: {func.__name__}")
        return func(username, *args, **kwargs)
    return wrapper

@log_action
def login(username):
    print(f"пользователь {username} вошёл в систему")