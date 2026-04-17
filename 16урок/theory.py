'''
Словари dict
принцип работы дейтсвет попарно
ключ - значение
'''
dict1 = {}
volor = dict(red="красный", blue="синий", black="чёрный")
person1 = {
    "name": "Владислав",
    "age" : "24", 
    "city": "Пермь",
    "familia" : "Кузнецов"
}
person2 = {
    "name": "Игорь",
    "age" : "12", 
    "city": "Пермь"
}
person3 = {
    "name": "Светлана",
    "age" : "70", 
    "city": "Пермь"
}
data = {
    "id":123,
    64:"шестдесят четыре",
    ("Анна",) : "кортеж как ключ",
    "score":[1,2,3,4],
}
'''for key, value in data.items():
    print(f"{key} : {value}")
'''
a = input("Что хотите знать?: ")
print(person1.get(a))
print(person2.get(a))
print(person3.get(a, "нет данных"))

familia = input("Что хотите знать?: ")
person2['familia'] = "Захарова"
print(f"{person2[a]}")