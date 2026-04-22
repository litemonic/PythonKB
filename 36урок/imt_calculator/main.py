from imt_calc import calculate_imt, isTrue, get_imt_category
import os

LOG_FILE = "imt_log.txt"

def get_next_number():
    if not os.path.isfile(LOG_FILE):
        return 1
    
    with open(LOG_FILE, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        if not lines:
            return 1
        
        last_line = lines[-1].strip
        if not last_line:
            return 1
        

        try:
            """Номер: x | Рост: 160 | Вес: 55 | ИМТ: 40 | лишний вес: ДА"""
            parts = last_line.split("|")
            num_parts = parts[0].strip()
            num = int(num_parts.split(":")[1].strip())
            return num + 1
        except:
            return 1
        
def save_to_txt(person_num, heitgh, weight, imt, status):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Номер: {person_num},| Рост: {heitgh}|Вес:{weight}|ИМТ:{imt}|Лишний вес:{status}")

def get_positive(promt):
    while True:
        try:
            value = float(input(promt))
            if value > 0:
                return value
            else:
                print("Значение должно быть больше 0")
        except ValueError:
            print("Ошибка: Введите число")

def main():
    print("Калькулятор ИМТ\n")

    weight = get_positive("Введите вес(кг)")
    height = get_positive("Введите рост(м)")

    imt = calculate_imt(weight, height)
    
    over_text = "Да" if isTrue else "None"
    person_num = get_next_number()
    save_to_txt(person_num, height, weight, imt, over_text )
    category = get_imt_category(imt)

    print(f"Результат для человека #{person_num}")
    print(f"Рост: {height} м")
    print(f"Вес: {weight}")
    print(f"ИМТ: {imt}")
    print(f"Лишний вес: {over_text}")
    print(f"Категория: {category}")
    print(f"Данные сохранены в файле: {LOG_FILE}")

    


if __name__ == "__main__":
    main()