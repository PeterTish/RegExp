from pprint import pprint
import re
import csv



with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # print(contacts_list)

    pattern_fio = r'([А-ЯЁ][а-яё]{2,})(\s|\W*)([А-ЯЁ][а-яё]{2,})\s([А-ЯЁ][а-яё]{2,})'
    fio = re.finditer(pattern_fio, str(contacts_list))
    fio_list = [i[0] for i in fio]
    sub_pattern_fio = r'\1 \3 \4'
    new_fio_list = re.sub(pattern_fio, sub_pattern_fio, str(fio_list))


    pattern_organization = r'[А-ЯЁ]{3,}|Мин[а-я]+'
    organization_list = re.findall(pattern_organization, str(contacts_list))


    pattern_phone = '(\+7|8)\s*\(*(\d{,3})\)*(\s|\W)*(\d{,3})-*(\d{,2})-*(\d+)\s*\(*(доб\.)*\s*(\d+)*\)*'
    phone_number = re.finditer(pattern_phone, str(contacts_list))
    phone_list = [i[0] for i in phone_number]
    sub_pattern_phone = r'+7(\2)\4-\5-\6\7\8'
    new_phone_list = re.sub(pattern_phone, sub_pattern_phone, str(phone_list))


    pattern_email = r'(?:[A-Za-z0-9.]+)@(?:[a-z0-9]+)\.(?:[a-z.]{2,})'
    email_list = re.findall(pattern_email, str(contacts_list))


    # new_contacts_list = []
    # for contact in contacts_list:
    #     contact_string = ','.join(contact)
    #     phone_sub = re.sub(pattern_phone, sub_pattern_phone, str(contacts_list))
    #     fio_sub = re.sub(pattern_fio, sub_pattern_fio, phone_sub)
    #     contact_list = fio_sub.split(',')
    #     new_contacts_list.append(contact_list)


    sub_contact_list = []
    for contact in contacts_list:
        phone_sub = re.sub(pattern_phone, sub_pattern_phone, str(contact))
        fio_sub = re.sub(pattern_fio, sub_pattern_fio, str(phone_sub))
        fio_sub = fio_sub.split('"')
        # print(fio_sub)
        sub_contact_list.append(fio_sub)






























