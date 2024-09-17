def search_paraments():
    parament = None
    var = input('По какому полю выполнить поиск? \n'
          '1 - название заметки, 2 - заметка \n'
          'Ваш выбор: ')
    if var == '1':
        parament = input('Введите название заметки: ')
    elif var == '2':
        parament = input('Введите заметку: ')
    return var, parament