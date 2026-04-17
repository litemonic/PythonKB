
from functools import wraps


def log_execution(func):
    wraps(func)
    def wrapper(user, *args, **kwargs):
        return func(user, *args, **kwargs)
    return wrapper

@log_execution
def add_log(user_func):
    with open("logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(user_func.get("name"))
        log_file.write(user_func.get("args"))

action_1 = {
    "name":"attack",
    "args":"15"
}
action_2 = {
    "name":"heal",
    "args":"25"
}

add_log(action_1)
add_log(action_2)