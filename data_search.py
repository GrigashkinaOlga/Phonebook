from search_paraments import search_paraments

def search_user_data():
   search_result = []   
   var, parament = search_paraments()
   contact_list = []
   new_contact_list = []
   with open('info.csv', 'r', encoding='utf-8') as file:
       for line in file.readlines():
           contact_list.append(line.strip().split())
   for i in contact_list:
       if i not in new_contact_list and len(i) == 4:
           new_contact_list.append(i)
    
   for contact in new_contact_list:
            if contact[int(var)-1] == parament:
                search_result.append(contact)
   if len(search_result) == 1:
       return search_result[0]
   elif len(search_result) > 1:
       print('Найдено несколько контактов')
       for i in range(len(search_result)):
           print(f'{i + 1} - {search_result[i]}')  
       num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
       return search_result[num_count - 1]
   
   else:
       print('Контакт не найден')
       print()
   
   
