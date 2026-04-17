person3 = {
    "name": "Светлана",
    "age" : "70", 
    "city": "Пермь",
    "red" : "красный",
    "blue" : "синий",
    "black" : "чёрный"
}
a = "city"
del person3 [a]
print(person3)

age = person3.pop("age")
print(age)

print(person3.popitem())
print(person3)

person3.clear()
print(person3)