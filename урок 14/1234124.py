'''nums = (1,2,2,2,2,3,4,4)
uniqList = []
for i in nums:
    if i not in uniqList:
        uniqList.append(i)
result = tuple(uniqList)
print(f"Отсортированный список {uniqList}")
    '''
nums = (1,23,4,6,8,0)
listik = list(nums)
maxElement = max(listik)
listik.remove(max(listik))
secondMaxElement = max(listik)
print(f"Второй по величине элемент: {secondMaxElement}")