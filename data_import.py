def import_data_info():

    with open ('info1.csv', 'r') as f:
       old_data = f.read()
       new_data = old_data.replace('\n', ' ')
       new1_data = new_data.replace('  ', '\n')
    with open ('info1.csv', 'w') as f:
        f.write(new1_data)

    with open ('info2.csv', 'r') as f:
       old_data = f.read() 
       new_data = old_data.replace(';', ' ')
    with open ('info2.csv', 'w') as f:
        f.write(new_data)  

    with open('info1.csv', 'a') as file:
        file.write('\n')        
    with open('info2.csv', 'a') as file:
        file.write('\n')     
    
    with open('info.csv', 'w') as outfile:
        for f in ['info1.csv', 'info2.csv']:
            with open(f, 'r') as infile:
                outfile.write(infile.read())

    pass

def import_data_info_1_2():

    with open ('info.csv', 'r') as f:
       old_data = f.read()
       new_data = old_data.replace('\n', '\n\n')
       new1_data = new_data.replace(' ', '\n')
    with open ('info1.csv', 'w') as f:
        f.write(new1_data)

    with open ('info.csv', 'r') as f:
       old_data = f.read()
       new_data = old_data.replace(' ', ';')
    with open ('info2.csv', 'w') as f:
        f.write(new_data)

    pass

