'''
sum = 0
while True:
    userInput = int(input("Введите числа(когда захотите остановится нажмите0, проргамма выведет сумму чисел): "))
    sum += userInput
    if userInput == 0:
        print(f"Сумма введенных чисел: {sum}")
        break


temp = float(input("Введите температуру(в градусах цельсия)"))
while True:
    choose = int(input("Что вы хотите сделать с этой температурой?\n1. перевести из Цельсия в Кельвины\n2. перевести из Цельсия в Фаренгейт.\n"))
    match choose:
        case 1:
            print(273.15 / temp + 273.15, " градусов по Кельвину. ")
            break
        case 2:
            print((temp * 9/5) + 32, " градусов по Фаренгейту. ")
            break
        case _:
            print("Вы написали вариант, которого нет, пожалуйста используйте существующие")


import random

num = random.randint(1, 100)

attempts = 0
guess = 0

print("Я загадал число от 1 до 100, попробуй угадать")
while num != guess:
    guess = int(input("Введи число: "))
    attempts += 1

    if guess < num:
        print("Ты не угадал. Моё число больше")
    elif guess > num:
        print("Ты не угадал. Моё число меньше")
print(f"Ты угадал. Я польщен. тебе понадобилось на это {attempts} попыток")

'''

import turtle

t = turtle.Turtle()

t.shape("turtle")
t.speed(10)
t.width(10)
t.color("blue")
t.circle(90)
t.penup()
t.forward(190)
t.pendown()
t.color("black")
t.circle(90)
t.penup()
t.forward(190)
t.pendown()
t.color("red")
t.circle(90)
t.penup()
t.right(90)
t.back(75)
t.right(90)
t.forward(90)
t.pendown()
t.color("green")
t.circle(90)
t.penup()
t.forward(190)
t.pendown()
t.color("yellow")
t.circle(90)
turtle.exitonclick()
