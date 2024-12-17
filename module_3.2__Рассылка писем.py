def send_email(message, recipient, *, sender="university.help@gmail.com"):
    email_rec = recipient.find("@")
    if email_rec <= 0:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса: ", sender, "на адрес: ", recipient)
    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ. Письмо успешно отправлено с адреса: ", sender, "на адрес: ", recipient)
send_email('Это сообщение для проверки связи', 'ineska@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
