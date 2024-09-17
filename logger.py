from note_create import  input_info
from note_search import search_note
from note_import import import_info, import_info_2

def input_note():
    name, text, data = input_info()

    with open('info.csv', 'a', encoding='utf-8') as file:     # a добавить
        file.write( f'{data}; {name}; {text}\n')
    print('Заметка сохранена')
    pass

def print_note():
    import_info()

    contact_list = []
    new_contact_list = []
    with open('info.csv', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            contact_list.append(line.strip().split())
        for i in contact_list:
            if i not in new_contact_list and len(i) == 4:
                new_contact_list.append(i)    
    new_contact_list.sort(key=lambda x: x[0])
    
    with open('info.csv', 'w', encoding='utf-8') as file:
        for contact in new_contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

    import_info_2()

    print('Заметки')
    with open('info.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
    pass


def change_note():
    import_info()
    contact_list = []
    new_contact_list = []
    with open('info.csv', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            contact_list.append(line.strip().split())
        for i in contact_list:
            if i not in new_contact_list and len(i) == 4:
                new_contact_list.append(i)

    number_to_change = search_note()
    if len(number_to_change) == 4:
        parament = None
        var = input('Что хотите изменить? \n'
          '1 - Название заметки \n'
          '2 - Тело заметки \n'
          'Ваш выбор: ')
        
        if var == '1':
            parament = input('Введите название заметки: ')
        elif var == '2':
            parament = input('Введите тело заметки: ')
    
        else:
            parament = input('Ошибка! Ваш выбор: ')


        new_contact_list.remove(number_to_change)
        number_to_change[int(var)] = parament
        new_contact_list.append(number_to_change)

        with open('info.csv', 'w', encoding='utf-8') as file:
            for contact in new_contact_list:
                line = ' '.join(contact) + '\n'
                file.write(line)
    
        import_info_2()
        print('Заметка сохранена')
    else: 
        print('Заметка не найдена')

    pass

def delete_note():

    import_info()

    contact_list = []
    new_contact_list = []
    with open('info.csv', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            contact_list.append(line.strip().split())
        for i in contact_list:
            if i not in new_contact_list and len(i) == 4:
                new_contact_list.append(i)        


    number_to_change = search_note()
    new_contact_list.remove(number_to_change)

    with open('info.csv', 'w', encoding='utf-8') as file:
        for contact in new_contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    
    import_info_2()
    print('Заметка удалена')

    pass

def find_note():
     
    import_info()
      
    number_to_change = search_note()

    print('; '.join(number_to_change))

    pass