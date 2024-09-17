from logger import input_note, print_note, change_note, delete_note, find_note 


def interface():
    print('Добрый день! Это бот помощник. \n'
          'Что вы хоите сдеать? \n'
          '1 - Создать новую замтку \n'
          '2 - Вывести все заметки \n'
          '3 - Найти и прочитать заметку \n'
          '4 - Изменить заметку \n'
          '5 - Удалить заметку')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 6:
        command = int(input('Ошибка! Ваш выбор: '))

    if command ==1:
        input_note()
    elif command ==2:
        print_note() 
    elif command ==3:
        find_note()      
    elif command ==4:
        change_note()        
    elif command ==5:
        delete_note()

interface()