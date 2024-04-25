from Lab_11.task1.task1 import Restaurant

# 11.2)	На основе ранее созданного класса Restaurant из задания 11.1
# создайте три разных экземпляра (три ресторана),
# вызовите для каждого экземпляра метод describe_restaurant().

restaurant_1 = Restaurant('Сытый ёж', 'Итальянская кухня')
restaurant_2 = Restaurant('Рыба моей мечты', 'Пельменная')
restaurant_3 = Restaurant('Мясорубка', 'Русская кухня')

if __name__ == '__main__':
    # restaurant_1.describe_restaurant()
    # restaurant_2.describe_restaurant()
    # restaurant_3.describe_restaurant()
    print(restaurant_1, restaurant_2, restaurant_3, sep='\n')
