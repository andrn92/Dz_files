def get_dictionary():
    dict_counters = {}
    list_counters = [0]*len(list_files)
    for i in range(len(list_files)):
        counter = 0
        with open(list_files[i], 'r', encoding='utf-8') as file_object:
            lst = file_object.readlines()
            for string in lst:
                counter += 1
            dict_counters[list_files[i]] = counter
            list_counters[i] = counter
    turple_1 = (dict_counters, list_counters)
    return turple_1

def sorted_list_files():
    turple_1 = get_dictionary()
    dict_counters = turple_1[0]
    list_counters = turple_1[1]
    list_counters.sort()
    for key, value in dict_counters.items():
        for i in range(len(list_counters)):
            if list_counters[i] == value:
                list_files[i] = key
    return list_files

def rewrite_file(parameter, i):
    list_files = sorted_list_files()
    turple_1 = get_dictionary()
    dict_counters = turple_1[0]
    with open(list_files[i], 'r+', encoding='utf-8') as f_object:
        lines = f_object.readlines()
        with open(file, parameter, encoding='utf-8') as file_object:
            for key, value in dict_counters.items():
                if key == list_files[i]:
                    file_object.write(key + '\n')
                    file_object.write(str(value) + '\n')
        for line in lines:
            with open(file, 'a+', encoding='utf-8') as f:
                f.write(line)

def get_result():
    fl = False
    for i in range(len(list_files)):
        if fl == False:
            rewrite_file('w+', i)
            fl = True
        elif fl == True:
            rewrite_file('a+', i)


file = '4.txt'
list_files = ['1.txt', '2.txt', '3.txt']
get_result()