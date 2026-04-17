text = "Python"
iterator = iter(text)
while True:
    try:
        step = next(iterator)
        print(step)
    except StopIteration:
        print("Строки закончились")
        break