numbers = [10, 20, 30, 40, 50]
numbers2 = list()
summa = numbers[0] + numbers[-1]
dif = numbers[2] - numbers[-2]
for i in range[4]:
    numbers2[i] = numbers[i]
numbers2[1] += 5
numbers2[-1] -=5
print("Сумма первого и последнего: ", summa)
print("Разница второго и предпоследнего: ", dif)
print("Изменённый список: ", numbers2)