from data_create import  input_user_data
from data_search import search_user_data
from data_import import import_data_info, import_data_info_1_2

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'В каком формате записать данные? \n'
                    f'1 вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    while var < 1 or var > 2:
        var = int(input('Ошибка! Ваш выбор: '))

    if var == 1:
        with open('info1.csv', 'a', encoding='utf-8') as file:     # a добавить
            file.write(f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n')

    elif var ==2:
        with open('info2.csv', 'a', encoding='utf-8') as file:     # a добавить
            file.write( f'{name};{surname};{phone};{adress}\n\n')
    pass

def print_data():
    
    print('1 файл: ')
    with open('info1.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

    print('2 файл: ')
    with open('info2.csv', 'r', encoding='utf-8') as file:     # r читать
        data = file.readlines()
        print(''.join(data))
    pass


def change_data():
    import_data_info()
    contact_list = []
    new_contact_list = []
    with open('info.csv', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            contact_list.append(line.strip().split())
        for i in contact_list:
            if i not in new_contact_list and len(i) == 4:
                new_contact_list.append(i)

    number_to_change = search_user_data()

    parament = None
    var = input('В какие данные хотите внести изменения? \n'
          '1 - Имя \n'
          '2 - Фамилия \n'
          '3 - Номер телефона \n'
          '4 - Адрес \n'
          'Ваш выбор: ')
    
    if var == '1':
        parament = input('Введите имя: ')
    elif var == '2':
        parament = input('Введите фмилию: ')
    elif var == '3':
        parament = input('Введите номер телефона: ')
    elif var == '4':
        parament = input('Введите адрес: ')
    
    else:
        parament = input('Ошибка! Ваш выбор: ')


    new_contact_list.remove(number_to_change)
    number_to_change[int(var)-1] = parament
    new_contact_list.append(number_to_change)

    with open('info.csv', 'w', encoding='utf-8') as file:
        for contact in new_contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    
    import_data_info_1_2()
    pass

def delete_data():

    import_data_info()

    contact_list = []
    new_contact_list = []
    with open('info.csv', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            contact_list.append(line.strip().split())
        for i in contact_list:
            if i not in new_contact_list and len(i) == 4:
                new_contact_list.append(i)        


    number_to_change = search_user_data()
    new_contact_list.remove(number_to_change)

    with open('info.csv', 'w', encoding='utf-8') as file:
        for contact in new_contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    
    import_data_info_1_2()

    pass