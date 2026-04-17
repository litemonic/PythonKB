
while True:
    def called_count(func):
        count = 0
        def wrapper(user, *args, **kwargs):
            nonlocal count
            count =+ 1
        return wrapper
    
    @called_count
    def view_count(count):
        print(count)

    view_count()