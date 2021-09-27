# почему меня не работает один без второго
from os import path
import os

# Задание 1

# вот тут какой-то магическический вариант получения той папки, где сейчас находится скрипт.
# на винде мой текстовый файл не вилится без такого кода, на макос видится - почему?
dir = path.dirname(path.abspath(__file__))

# заменяем рабочую директорию на папку с файлом
os.chdir(dir)

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as recipes:
    for line in recipes:
        recipe = line.strip()
        count = int(recipes.readline())
        ingridients = []

        for i in range(count):
            ingredient_name, quantity, measure = recipes.readline().split(' | ')
            ingridients.append({'ingredient_name': ingredient_name.strip(),'quantity':quantity.strip(), 'measure':measure.strip()}) 

            cook_book[recipe] = ingridients
        recipes.readline()

# Задание 2
# тут создаём список всех блюд
all_dishes = []
for keys, values in cook_book.items():
    all_dishes.append(keys)

# функция будет тут

def get_shop_list_by_dishes(all_recept, person_count):
    all_need_ing = {}
    for need_dishes in all_recept:
        for recept, need_ing in cook_book.items():
            if need_dishes == recept:
                for items in need_ing:
                    if items['ingredient_name'] not in all_need_ing:
                        all_need_ing[items['ingredient_name']] = {'measure': items['measure'], 'quantity' : (int(items['quantity'])) * 2} 
                    else:
                        all_need_ing[items['ingredient_name']]['quantity'] = all_need_ing[items['ingredient_name']]['quantity'] + (int(items['quantity']) * person_count)
    print(all_need_ing)

                
# get_shop_list_by_dishes(all_dishes, 2)
    
    

# Задание 3

# получаем количество строк

os.chdir('files')

stage_list = {}

# выводит весь список файлов в папке
for file in os.listdir():
    if '.txt' in file:
            with open(file, 'r', encoding='utf-8') as first_txt:
                first_file = [row.rstrip() for row in first_txt]
                # print(file)
                # print(len(first_file))
                stage_list[file] = len(first_file)

sorted_stage_list = dict(sorted(stage_list.items(), key=lambda x: x[1]))
print(sorted_stage_list)

for files, stroke in sorted_stage_list.items():
    with open(files, 'r', encoding='utf-8') as read_file:
        with open('endfile.txt', 'a', encoding='utf-8') as write_file:
            for item in range(stroke):
                print(read_file.readline())
                write_file.write(read_file.readline())

            











        






