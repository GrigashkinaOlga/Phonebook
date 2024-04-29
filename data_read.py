def read_user_data():

    with open('info.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Имя', 'Фамилия', 'Номер телефона', 'адрес']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

    
