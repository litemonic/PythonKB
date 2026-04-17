'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

match a < b and c != d:
    case True:
        print("Правда")
        if a == 12:
            print("ЛАЛАЛА")
            summ = a+b+c+d
            match summ:
                case 10:
                    print("ДЕСЯТЬ")
        else:
            print("НЕ 12")
    case False:
        if c < a:
            print("hahaha")
        print("Ложь")
'''
num = input()
match num:
    case 1:
        print("afawf")
    case "2":
        print("ddd")