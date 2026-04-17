def spisikReturn(spisik = []):
    reslist = []
    a = max(spisik)
    for index, value in enumerate(spisik, 1):
        if value == a:
            reslist.append(index)
            reslist.append(a)
            break
    return reslist
print(spisikReturn([1,2,3,10,3,4,5]))