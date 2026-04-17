num = (2,5,7,1,7,9)
i = 0
target = 7
while i < len(num):
    if num[i] == target:
        print(f"число 7 первый раз встречается на {i+1} элементе")
        break
    else:
        i+=1

