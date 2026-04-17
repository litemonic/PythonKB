while True:
    try:
        choose = input("Вы хотите войти в аккаунт или зарегистрироваться? (1-зарегистрироваться, 2-залогиниться )")
        match choose:
            case "1":
                login = input("Введите логин")
                password = input("Введите пароль")
                checkLog = login
                checkPassw = password
                age = int(input("Введите свой возвраст."))
                isRobot = input("Вы робот?").lower()
                match age:
                     case age if age <= 0:
                        print("Вижу, что вы балуетесь. Программа завершена.")
                        break
                     case age if age > 150:
                        print("О, похоже вы рекордсмен по продолжительности жизни. Программа для вас закрыта.")
                        break
                     case age if age >= 16:
                        match isRobot:
                                case"нет":
                                    print("Вам предоставлен доступ. Залогиньтесь чтобы войти в систему")
                                    continue   
                                case"да":
                                    print("Вам не предоставлен доступ.")
                                case _:
                                    print("Введите 'да' или 'нет'")
                        break
                     case _:
                        print("Вы не подходите по воврасту.")
                        break
            case "2":
                login = input("Введите логин")
                match checkLog == login:
                        case True:
                            match checkPassw == password:
                                case True:
                                    print("Вы можете наслаждаться сайтом.")
                                    break
                                case False:
                                    print("Неверный пароль.")
                                    continue
                        case False:
                            print("Неверный логин.")
                            continue
            case _:
                  print("Введите 1 или 2.")
                  continue
    except Exception as e:
        print(f"Произошла ошибка {e}")
        print(f"Тип ошибки: {type(e),__name__}")


                 

