userInput = input("Введите слово, которое хотите вывести в обратном порядке.")
reverseWord = ""
for i in range(len(userInput)- 1, -1, -1):
    reverseWord += userInput[i]
    print(reverseWord)
'''
[начало:конец:шаг]
'''
print(input("Введите слово: "[::-1]))
