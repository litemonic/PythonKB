import random
lst = [random.randint(1,100) for _ in range(10)]
def RandomNumOrder(spisik = []):
    for index, _ in enumerate(spisik):
        if index % 2 == 0:
            for _ in range(len(spisik)):
                if spisik[index] < spisik[index+1] and index + 1 < len(spisik):
                    spisik[index] = spisik[index+1]
        else:
            for _ in range(len(spisik)):
                if spisik[index] > spisik [index+1] and index + 1 < len(spisik):
                    spisik[index+1] = spisik[index]
    return spisik
print(lst)
print(RandomNumOrder(lst))
