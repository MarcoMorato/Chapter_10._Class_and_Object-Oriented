import cellphone


def main():
    phone = make_list()
    display_list(phone)


def make_list():
    phone_list = []
    for count in range(1, 3):
        print('Номер телефона', count,':')
        man = input('Производитель ')
        mod = input('Модель ')
        retail = float(input('Цена '))
        phone = cellphone.CellPhone(man, mod, retail)
        phone_list.append(phone)
    return phone_list


def display_list(list):
    for x in list:
        print(x)



main()
