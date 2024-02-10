import csv

"""По списку транзакций находйти пользователя, купившего больше всех билетов
и вывести количество билетов. Пользователь - совпадение email и телефона (у одного пользователя 
может быть несколько номеров или почт)"""

transaction = {}
mails = {}
phones = {}

with open("transaction_logs.csv", "r") as csv_file:
    csvreader = csv.reader(csv_file)
    i = 1
    for row in csvreader:
        mail, phone = row[0], row[1]
        if mail not in mails and phone not in phones:
            mails[mail] = i
            phones[phone] = i
            transaction[i] = 1
            i += 1
        elif mail in mails and phone not in phones:
            user = mails.get(mail)
            phones[phone] = user
            quantity = transaction.get(user)
            transaction[user] = quantity + 1
        elif mail not in mails and phone in phones:
            user = phones.get(phone)
            mails[mail] = user
            quantity = transaction.get(user)
            transaction[user] = quantity + 1
        elif mail in mails and phone in phones:
            user_mail_id = mails.get(mail)
            user_phone_id = phones.get(phone)
            if user_mail_id == user_phone_id:
                quantity = transaction.get(user_phone_id)
                transaction[user_mail_id] = quantity + 1
            else:
                mails[mail] = user_phone_id
                for k, v in phones.items():
                    if user_mail_id == v:
                        phones[k] = user_phone_id
                for k, v in mails.items():
                    if v == user_mail_id:
                        mails[k] = user_phone_id
                old_quantity = transaction.get(user_mail_id)
                exist_quantity = transaction.get(user_phone_id)
                transaction[user_phone_id] = old_quantity + exist_quantity + 1
                del transaction[user_mail_id]

print(max(v for v in transaction.values()))
