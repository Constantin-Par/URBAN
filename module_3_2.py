def send_email(message, recipient, *, sender="university.help@gmail.com"):

    str_r = recipient.lower()
    str_s = sender.lower()

    ext_r = str_r[str_r.rfind('.'):len(str_r)]  # домен получателя
    ext_s = str_s[str_s.rfind('.'):len(str_s)]  # домен отправителя
    ext = ['.com', '.net', '.ru']  # разрешенные домены

    if not ext_r in ext or not ext_s in ext or str_s.find('@') == -1 or str_r.find('@') == -1:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if str_r == str_s:
        print('Нельзя отправить письмо самому себе!')
        return

    if str_s == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
