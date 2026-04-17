def range_with_step(start, end, step):
    count = start
    while count < end:
        yield count
        count += step

start = int(input("начало: "))
end = int(input("конец: "))
step = int(input("шаг: "))

print(range_with_step(start, end, step))