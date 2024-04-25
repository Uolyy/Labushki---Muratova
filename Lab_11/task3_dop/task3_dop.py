from icecream import ic
import os
from Lab_11.task1.task1 import Restaurant

# 11.1)	Добавьте в созданный класс Restaurant атрибут,
# задающий начальный рейтинг ресторана и метод,
# который получает на вход новое значение рейтинга и обновляет его.

with open('rating', 'a', encoding='utf') as file:
    try:
        rating = float(input('Введите рейтинг ресторана: ').replace(",", "."))

        if 1.0 <= rating <= 5.0:
            if os.stat('rating').st_size == 0:  # проверяет, пустой файл или нет
                file.write(f'{rating}')
            else:
                file.write(f', {rating}')
        else:
            print('Оценка может быть в диапазоне от 1 до 5 включительно')
            exit()
    except ValueError:
        print("Введена строка вместо числа")
        exit()


current_rating = 0
with open('rating', 'r', encoding='utf') as file:
    line = file.readline()
    values = line.strip().split(',')
    # ic(len(values))

    for value in values:
        current_rating = current_rating + float(value)
        # ic(float(value))

    current_rating /= len(values)

restaurant_4 = Restaurant('Котофея', 'Японская кухня')
restaurant_4.set_rating(current_rating)
# restaurant_4.describe_restaurant()
print(restaurant_4)
restaurant_4.open_restaurant()

print(f'Рейтинг ресторана {restaurant_4.restaurant_name}: {current_rating:.2f}')
