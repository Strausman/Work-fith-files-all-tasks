# Задание 1
def read_recipe_file(file_path):
    cook_book = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                dish_name = file.readline().strip()
                if not dish_name:  # Конец файла
                    break

                ingredients_count = int(file.readline().strip())
                ingredients_list = []
                for _ in range(ingredients_count):
                    ingredient_str = file.readline().strip()
                    ingredient_name, quantity, measure = ingredient_str.split(' | ')
                    ingredients_list.append({
                        'ingredient_name': ingredient_name,
                        'quantity': int(quantity),
                        'measure': measure
                    })

                cook_book[dish_name] = ingredients_list
                file.readline()  # Пропуск пустой строки между рецептами
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    return cook_book
cook_book = read_recipe_file('recipes.txt')
# print(cook_book)




# Задание 2

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ]
    }
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': ingredient['quantity'] * person_count}
    return shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
# print(shop_list)
# for ingredient, details in shop_list.items():
#     print(f"{ingredient}: {details['measure']} {details['quantity']}")




# Задание 3

def count_lines_in_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return sum(1 for i in file)

def sort_files_by_lines(file_names):
    return sorted(file_names, key = count_lines_in_file)

def merge_files_sorted_by_lines(file_names, output_file_name):
    sorted_file_names = sort_files_by_lines(file_names)
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        for file_name in sorted_file_names:
            lines_count = count_lines_in_file(file_name)
            output_file.write(f"{file_name}\n{lines_count}\n")
            with open(file_name, 'r', encoding='utf-8') as input_file:
                output_file.writelines(input_file)
            output_file.write("\n")

file_names = ['1.txt', '2.txt', '3.txt']
output_file_name = 'result.txt'
merge_files_sorted_by_lines(file_names, output_file_name)





