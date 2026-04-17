'''
slovo1 = set("программирование")
slovo2 = set("алгоритм")

bothWords = slovo1 & slovo2
onlyFirst = slovo1 - slovo2
onlySecond = slovo2 - slovo1

password = ''.join(sorted(bothWords)) + ''.join(sorted(onlyFirst)) + ''.join(sorted(onlySecond))

print(password)
'''

otdelA = {"Иванов", "Петров", "Сидоров"}
otdelB = {"Козлов", "Петров", "Смирнов"}
otdelC = {"Иванов", "Смирнов", "Кузнецов"}

mostPass = otdelA & otdelB & otdelC
OnlyOne = otdelA ^ otdelB ^ otdelC
cannot = otdelA - otdelB - otdelC
onlyPetrov = ""
try:
    otdelA.remove("Петров")
except:
    onlyPetrov += "ОтделА"
try:
    otdelA.remove("Петров")
except:
    onlyPetrov += "ОтделВ"
try:
    otdelA.remove("Петров")
except:
    onlyPetrov += "ОтделС"

print(f"Все пропуски есть у: {mostPass if mostPass else "На данный момент таких людей нет."}")
print(f"Только к одному отделу доступ есть у: {OnlyOne if OnlyOne else "На данный момент таких людей нет."}")
print(f"Ни к одному отделу нет доступа у {cannot if cannot else "На данный момент таких людей нет."}")
print(f"У Петрова есть доступ к {onlyPetrov if onlyPetrov else "никаким."}")

'''
if "Петров in otdelA: onlyPetrov.append("A")
if "Петров in otdelB: onlyPetrov.append("B")
if "Петров in otdelC: onlyPetrov.append("C")
print(" ".join(onlyPetrov) if onlyPetrov else "нет таких.")
'''