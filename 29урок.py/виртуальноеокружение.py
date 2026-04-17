l = 7
h = 7

def AOfDots(length, heigth):
    mid = length // 2

    for i in range(heigth):
        for j in range(length):
            if i == 0 and j == mid or \
            (i > 0 and j==0) or \
            (i > 0 and j == length-1) or \
            (i > 0 and i ==mid):
                print("*",end="")
            else:
                print(" ",end="")
        print()
AOfDots(l,h)    