list_files = ['1.txt', '2.txt', '3.txt'] 
file = '4.txt'
dict_counters = {}
for i in range(len(list_files)):
    counter = 0
    with open(list_files[i], 'r', encoding='utf-8') as file_object:
        lst = file_object.readlines()
        for string in lst:
            counter += 1
        dict_counters[list_files[i]] = counter
       
fl = False
for i in range(len(list_files)):
    if fl == False:
        with open(list_files[i], 'r+', encoding='utf-8') as f_object:
            lines = f_object.readlines()
            with open(file, 'w+', encoding='utf-8') as file_object:
                for key, value in dict_counters.items():
                    if key == list_files[i]:
                        file_object.write(key + '\n')
                        file_object.write(str(value) + '\n')
            for line in lines:
                with open(file, 'a+', encoding='utf-8') as f:
                    f.write(line)
            fl = True
    elif fl == True:
        with open(list_files[i], 'r+', encoding='utf-8') as f_object:
            lines = f_object.readlines()
            with open(file, 'a+', encoding='utf-8') as file_object:
                for key, value in dict_counters.items():
                    if key == list_files[i]:
                        file_object.write(key + '\n')
                        file_object.write(str(value) + '\n')
            for line in lines:
                with open(file, 'a+', encoding='utf-8') as f:
                    f.write(line)
                