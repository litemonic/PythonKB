person3 = {
    "name": "Светлана",
    "age" : "70", 
    "city": "Пермь",
    "red" : "красный",
    "blue" : "синий",
    "black" : "чёрный"
}
print(list(person3.values()))
for keys, value in person3.items():
    print(f"{keys} : {value}")

city = person3.setdefault("city") # добавление ключа если отсутствует
print(city)