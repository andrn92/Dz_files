cook_book = {}
lst = []
dict_ingredients = {}
with open('Example/data3.txt', 'r') as cook_book_list:
    for line in cook_book_list:
        foods_name = line[:-1]
        count_foods = cook_book_list.readline()
        for i in range(int(count_foods)):
            ingredients = cook_book_list.readline()
            name, quantity, measure = ingredients.split(' | ')
            dict_ingredients['ingredient_name'] = name
            dict_ingredients['quantity'] = quantity
            dict_ingredients['measure'] = measure[:-1]
            lst.append(dict_ingredients)
            dict_ingredients = {}
        cook_book[foods_name] = lst
        lst = []
        cook_book_list.readline()


print(cook_book)

