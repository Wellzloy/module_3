# def send_email(message, recipient, sender = "university.help@gmail.com"):
#     if recipient __contains__('@')
recipient = 'vasyok1337@gmail.com'
sender = 'vasyok1337@mail.ru'

# print('recipient', recipient.__contains__('@'))

if '@' in recipient and recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
    if '@' in sender and sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
        pass
    else:
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
else:
    print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
