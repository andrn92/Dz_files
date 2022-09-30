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


new_dict = {}
def get_shop_list_by_dishes(list_dishes, person_count):
    for dish, ingredients_list in cook_book.items():
        for dict_ingredients in ingredients_list:
            if dish in list_dishes:
                ingredient_name = dict_ingredients['ingredient_name']
                measure = dict_ingredients['measure']
                quantity = int(dict_ingredients['quantity'])
                new_dict[ingredient_name] = {'measure': measure, 'quantity': quantity * person_count}
    print(new_dict)

list_dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
get_shop_list_by_dishes(list_dishes, person_count)
