from icecream import ic
from pprint import pprint

# 9.3) Имеется файл с данными в формате csv:
# Продукт,Количество,Цена
# Молоко,2,80
# Сыр,1,500
# Хлеб,2,70
# Напишите программу, которая считывает данные из этого файла, подсчитывает итоговую сумму расходов и выводит:
# Нужно купить:
# Молоко - 2 шт. за 80 руб.
# Сыр - 1 шт. за 500 руб.
# Хлеб - 2 шт. за 70 руб.
# Итоговая сумма: 800 руб.

eda: dict = {}
with open('edaedaeda.csv', encoding='utf') as f:
    data = f.readlines()  # data - list[str]
    data.pop(0)
    for item in data:
        item = item.split(',')
        eda[item[0]] = {'количество': int(item[1]), 'цена': int(item[2])}
        # ic(eda)
    pprint(eda, sort_dicts=False)

print('Нужно купить: \n')
price: int = 0
for product in eda:
    price += eda[product]['цена'] * eda[product]['количество']
    print(f'{product} — {eda[product]["количество"]} шт. за {eda[product]["цена"]} руб.')
print(f'\nОбщая сумма: {price} руб.')
