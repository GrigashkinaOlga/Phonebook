def search_paraments():
    parament = None
    var = input('По какому полю выполнить поиск? \n'
          '1 - имя, 2 - фамилия \n'
          'Ваш выбор: ')
    if var == '1':
        parament = input('Введите имя: ')
    elif var == '2':
        parament = input('Введите фамилию: ')
    return var, parament