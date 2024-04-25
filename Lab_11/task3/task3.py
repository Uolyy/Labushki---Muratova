from Lab_11.task1.task1 import Restaurant

# 11.1)	Добавьте в созданный класс Restaurant атрибут,
# задающий начальный рейтинг ресторана и метод,
# который получает на вход новое значение рейтинга и обновляет его.

restaurant_4 = Restaurant('Котофея', 'Японская кухня')
restaurant_4.set_rating(float(input('Введите рейтинг ресторана: ')))
# restaurant_4.describe_restaurant()
print(restaurant_4)
restaurant_4.open_restaurant()

print(f'Рейтинг ресторана {restaurant_4.restaurant_name}: {restaurant_4.rating}')
