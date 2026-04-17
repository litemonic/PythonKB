def simple_numbers(limit):
    spisik = []
    for i in range(limit):
        if i % i == 1 and i % 1 == i:
            spisik.append(i)
    yield spisik

limit = int(input("Введите лимит: "))
print(simple_numbers(limit))