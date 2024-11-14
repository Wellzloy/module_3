# def send_email(message, recipient, sender = "university.help@gmail.com"):
#     if recipient __contains__('@')
recipient = 'vasyok1337@gmail.com'
sender = 'vasyok133@mail.ru'
if '@' not in recipient:
    print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
elif '@' not in sender:
    print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
elif not (recipient.endswith('.com') or  recipient.endswith('.ru') or recipient.endswith('.net')):
    print('Окончание Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
else:
    print('Первую проверку прошли')

#print(not recipient.endswith('.com')) or not recipient.endswith('.ru') or not recipient.endswith('.net')): #and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
#     pass
    #if '@' in sender: #and sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):

   #else:
        #print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
