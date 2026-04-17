import random


characters = ['1','2','3','4','5','6','7','8','9','0',
                  'q','w','e','r','t','y','u','i','o','p',
                  'a','s','d','f','g','h','j','k','l',
                  'z','x','c','v','b','n','m']
lenght = int(input("Сколько символов вы хотите видеть в своем пароле: "))

if lenght < 6:
    lenght = 6
elif lenght > 20:
    lenght = 20

password = ''
for i in range(lenght):
    password += random.choice(characters)
print(f"Ваш пароль: {password}")
print(f"Длина пароля: {len(password)}")

