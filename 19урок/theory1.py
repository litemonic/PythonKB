number = int(input()) 
def skvadrat(number):
    if number < 0:
        pass
    else:
        resultat = number ** 2
        return resultat
resultat = skvadrat(number)
print(resultat)