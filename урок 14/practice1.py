animals = tuple(range(1,21))
animalsList = []

for animal in animals:
    if animal % 2 == 0:
        animalsList.append(animal)
evel = tuple(animalsList)
print(f"Исходный кортеж: {animalsList}")
print(f"Четный кортеж: {evel}")

nums = tuple(range(0,26))
evel = tuple(i for i in nums if i % 2 == 0)
print(f"Четный кортеж: {evel}")