def sumOfPair(a, b):
    len1, len2 = len(a), len(b)
    maxLen = max(len1, len2)
    total = 0
    for i in range(maxLen):
        elem1 = a[i % len1]
        elem2 = b[i % len2]
        total += elem1 * elem2
    return total

a = [1,2,3]
b = [4,5]
res = sumOfPair(a, b)
print(f"Сумма попарных произведений равна {res}")
