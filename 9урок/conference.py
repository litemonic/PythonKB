memberType = int(input("Выберите тип участника (1 - спикер, 2 - студент, 3 - гость, 4 - пресса): "))
isRegistated = input("Вы зарегистрированы? (да/нет)").lower()
age = int(input("Введите свой возвраст."))
isOrganisator = input("Вы организатор? (да/нет)").lower()    

secret = 123456789
if age < 18:
     print("Вам дожно быть больше 18 лет.")
elif isOrganisator == "да":
     print("Вы проходите.")
elif memberType == 3:
    if age >= 18 and isRegistated == "да":
         code = int(input("Введите код доступа"))
         if code == secret:
              print("Вы можете пройти")
         else:
              print("В доступе отказано. Неправильный код")
    else:
         print("В доступе отказано, вы не подходите по условиям для входа.")
elif memberType == 1:
     if isRegistated == "да":
          print("Вы проходите")
     else:
          print("Чтобы пройти, вам нужно зарегистрироваться") 
elif memberType == 4:
     if isRegistated == "да":
          print("Вы проходите")
     else:
          print("Чтобы пройти, вам нужно зарегистрироваться") 
elif memberType == 2:
    if age >= 18 and isRegistated == "да":
         print("Вы проходите")
    else:
         print("В доступе отказано, вы не подходите по условиям для входа.")
else:
     print("Вы не зарегистрированы в базе. Вы не проходите.")       
         
              
              
