def prsl(name):
    for i in range(4):
        print(f"Привет {name}")

name = input("Как тебя зовут?").strip()
prsl(name)