from pprint import pprint
import re
import csv

# [А-ЯЁ][а-яё]{2,}\s[А-ЯЁ][а-яё]{2,}\s[А-ЯЁ][а-яё]{2,}

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

    pattern_fio = r'(([А-ЯЁ][а-яё]{2,})\s?\b)'
    fio_list = re.findall(pattern_fio, str(contacts_list))

    pattern_organization = '[А-ЯЁ]{3,}|Мин[а-я]+'
    organization_list = re.findall(pattern_organization, str(contacts_list))

    pattern_phone = "((\+7|8?)\s?\(?\d+\)?\W?\d+\W?\d+[^']\d+\s?\(?...?[^']?\s?[0-9]+\)?)"
    phone_number = re.findall(pattern_phone, str(contacts_list))
    phone_list = [i[0] for i in phone_number]

    print(fio_list)
    # print(organization_list)
    # print(phone_list)






