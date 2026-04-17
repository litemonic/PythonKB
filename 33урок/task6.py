def repeat_message(message, times):
    for _ in range(times):
        yield print(message)
message = input("Введите сообщение: ")
times = input("Введите количество повторений: ")
repeat_message(message, times)