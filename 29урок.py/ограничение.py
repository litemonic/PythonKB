userinput = int(input("числа: "))
def NumberTimesFour(a):
    for i in range(1, a + 1):
        resOfumn = i*4
        strA = str(i)
        strResOfumn = str(resOfumn)

        if len(strA) == len(strResOfumn) and strA == strResOfumn[::-1]:
            print(f"Подходит: {i} * 4 = {resOfumn}")
NumberTimesFour(userinput)              
