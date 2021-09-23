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
all_recept = []
for keys, values in cook_book.items():
    all_recept.append(keys)

# функция будет тут
all_need_ing = {}
for need_dishes in all_recept:
    for recept, need_ing in cook_book.items():
        if need_dishes == recept:
            for items in need_ing:
                if items['ingredient_name'] not in all_need_ing:
                    all_need_ing[items['ingredient_name']] = {'measure': items['measure'], 'quantity' : int(items['quantity'])} 
                else:
                    all_need_ing[items['ingredient_name']].setdefault('quantity', int(items['quantity']))
                # не соединяет нефига сука

                
print(all_need_ing)
    
    


# Если в ключе cook_book есть нужное блюдо
# то пускаем цикл по значению ключа этого блюда, а там список и внутри снова словари
# мы тогда ingredient_name пишем ключем need_ing, а в значение списываем 'quantity': '100', 'measure': 'мл'
# Если такого значения еще не было, а если есть, то к прошлым суммируем.
        






