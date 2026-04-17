from calc import basic, advanced
from utils import formater, loger
from datetime import datetime

def main():
    try:
        loger.logInfo("Программа запущена")

        filename = "calculatorHistory.txt"
        file = open(filename, "a", encoding="utf-8")

        file.write(f"\n ---{datetime.now()}---")

        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию: ")
        if operation != "$":
            num2 = float(input("Введите второе число: "))
            if operation == "+":
                result = basic.add(num1,num2)
                print(formater.formatResult(f"{num1} + {num2}", result))
                text = f"{num1} {operation} {num2} = {result}"
            elif operation == "-":
                result = basic.substract(num1,num2)
                print(formater.formatResult(f"{num1} - {num2}", result))
                text = f"{num1} {operation} {num2} = {result}"
            elif operation == "*":
                result = basic.myltiply(num1,num2)
                print(formater.formatResult(f"{num1} * {num2}", result))
                text = f"{num1} {operation} {num2} = {result}"
            elif operation == "/":
                result = basic.divide(num1,num2)
                print(formater.formatResult(f"{num1} / {num2}", result))
                text = f"{num1} {operation} {num2} = {result}"
            elif operation == "**":
                result = advanced.power(num1,num2)
                print(formater.formatResult(f"{num1} ** {num2}", result))
                text = f"{num1} {operation} {num2} = {result}"
        if operation == "$":
                result = advanced.sqrt(num1)
                print(formater.formatResult(f"Кв. корень числа {num1}", result))
                text = f"Кв. корень числа {num1} = {result}"
        file.write(text)
        file.close
        loger.logInfo(f"История действий в файле : {filename}")
    except Exception as e:
        loger.errorInfo(e)
        filenameError = "Error.txt"
        file = open(filenameError, "a", encoding="utf-8")
        file.write(f"\n ---{datetime.now()}---")
        file.write(str(e))
        file.close
        loger.logInfo(f"История ошибок в файле : {filenameError}")

    loger.logInfo("Программа завершена")
if __name__ == "__main__":
    main()