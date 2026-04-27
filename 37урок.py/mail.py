import re
contacts = {
    "ivanov.ivan@gmail.com" : "Иванов Иван",
    "maria.ivanovna@yandex.com" : "Ивановна Мария",
    "alexey.smirnov@mail.ru" : "Смирнов Алексей",
    "dmitry.nagiev@bk.com" : "Нагиев Дмитрий"
}

def validate_email(email):
    pattern = f"^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True, "Формат email правильный"
    else:
        if "@" not in email:
            return False, "В email должен 100% быть знак @"
        
        parts = email.split("@")
        if len(parts) != 2: 
            return False, "Неверный формат данных"
        
        login, domain = parts

        if not login:
            return False, "Нет такого логина"
        if not domain:
            return False, "Нет такого домена"
        if "." not in domain:
            return False, "В домене должна быть точка"
        if re.search("^[&^{}()]", login):
            return False, "Имя пользователя содержит недопустимые символы"
        if re.search("^[0-9]$", domain.split()):
            return False, "Домен пользователя содержит недопустимые символы"
        tid = domain.split(".")[-1]
        if len(tid) < 3 or len(tid) > 6:
            return False, "Неверная длина доменного имени"
        
        return False, "email несоответствует правилам написания"
def checkInContacts(email):
    email_lower = email.lower()

    if email_lower in contacts:
        return True, f"Найден контакт: {contacts[email_lower]}"
    else:
        similar = []
        for contact_email, contact_name in contacts.items():
            if email_lower in contact_email or contact_email in email_lower:
                similar.append(f"{contact_name}, ({contact_email})")
        if not similar:
            return False, "Email не найден, возможно вы имели ввиду: ", similar
        else:
            return False, "Email нет в списке ваших контактов"
        
def send_email(from_email, to_email, subject, message):
    print("\n", "-"*50)
    print("Отправка письма")
    print("="*50)

    print(f"От кого: {from_email}")
    print(f"Кому: {to_email} ({contacts.get(to_email.lower(), "Контакт не найден")})")
    print(f"Тема: {subject}")
    print(f"Сообщение: {message}")

    print("="*50)
    print("Сообщение отправлено")
    print("="*50)

def main():
    print("Программа для отправки писем")
    print("\nВаши контакты")
    for i, (email, contact) in enumerate(contacts.items(),1):
        print(f"{i}. {email}")
    print("Выберите Email получателя")

    while True:
        rec_email = input("Введите email")
        is_valid_format, format_message = validate_email(rec_email)
        print(f"{format_message}")

        if not is_valid_format:
            print("Пожалуйста введите корректный формат почты")
            continue
        
        is_in_contacts, contact_message = checkInContacts(rec_email)
        print(f"{contact_message}")

        if is_in_contacts:
            break
        else:
            #Здесь могла быть возможность добавления в контакты
            pass
        print("Введите тему сообщения")
        subject = input("Тема: ").strip()

        if not subject:
            subject = "Без темы"
        
        lines = []
        while True:
            line = input()
            if line == "" and len(lines) > 0:
                break
            if line == "" and len(lines) == 0:
                continue
            lines.append(line)
        message = "\n".join(lines)

        if not message:
            message = "Текст отсутсвует"

        sender_email = input(f"Ваш email: ").strip()

        is_valid, message = validate_email(sender_email)
        if not is_valid:
            print(f"Ошибка: {message}")
            return
        send_email(sender_email, rec_email, subject, message)

if __name__ == "__main__":
    print("Главное меню")

    choice = input("Выберите действие: ")

    if choice == 1:
        main()     
    else:
        print("Неправильный выбор")
