step = int(input("Введите шаг: "))
start = int(input("Укажите начало: "))
end = int(input("Укажите конец: "))

spisik = [1,2,3,4]

step_iterator = iter(range(start, end, step))
while True:
    try:
        for _ in range(start, end + 1, step):
            num = next(step_iterator)
            print(num)
    except StopIteration:
        print("список закончился.")
        break