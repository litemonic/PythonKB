def isIdentical(s1, s2):
    
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                return False
        return True
    return False
s1 = [1, 2, 3]
s2 = [1, 2]
print(f"Сравниваем {s1} и {s2}, ответ: {isIdentical(s1, s2)}")

