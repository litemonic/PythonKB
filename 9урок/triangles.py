print("-"*10)
print("классификация треугольника и его свойств")
print("-"*10)

firstSide = float(input("Введите первую сторону треугольника: "))
secondSide = float(input("Введите вторую сторону треугольника: "))
thirdSide = float(input("Введите третью сторону треугольника: "))

if firstSide > secondSide + thirdSide:
    print("треугольник возможный.")
elif secondSide > firstSide + thirdSide:
    print("треугольник возможный.")
elif thirdSide > firstSide + secondSide:
    print("треугольник возможный.")
else:
    print("треугольник невозможный.")
if firstSide == secondSide == thirdSide:
    print("треугольник равносторонний.")
elif thirdSide == secondSide or secondSide == firstSide or firstSide == thirdSide:
    print("треугольник равнобедренный.")
elif firstSide != secondSide != thirdSide:
    print("треугольник разносторонний.")
