def report(text, index = 0):
    if index >= len(text):
        return
    print(text[index], end="")
    report(text, index + 2)

text = "Программирование"
print("Символы через один")
print(report(text))
