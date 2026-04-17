'''
    numberOfSum1 = 1
numberOfSum2 = 1
numberOfItterations = int(input("Введите индекс числа фибаначи"))
for i in range(numberOfItterations):
    sum = numberOfSum1 + numberOfSum2
    numberOfSum2 = numberOfSum1
    numberOfSum1 = sum
print(sum)
'''
num = 1
res = 1
rangeNum = int(input("Введите число, из которого будет высчитан факториал: "))
for i in range(rangeNum):
    res = res * num
    num += 1

print(res)
