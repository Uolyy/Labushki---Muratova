from Lab_11.task1.task1 import Restaurant




# 12.2) Модифицируйте ранее созданный IceCreamStand:
# 	1. Добавьте атрибуты для описания локации и времени работы кафе-мороженого
# 	2. Реализовать методы для добавления и удаления сортов мороженого из списка flavors
# 	3. Реализовать метод проверки наличия определенного сорта мороженого в списке flavors
# 	4. Добавить методы для разных типов мороженого (например, мороженое на палочке, мягкое мороженое и т.д)
# 	и реализовать методы для работы с каждым типом

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors, cuisine_type='мороженое'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print(f'Вкусы: {', '.join(self.flavors)}')


if __name__ == '__main__':
    flavor = ['Шоколад-банан', 'Лимон-мята', 'Малина-мёд']
    IceCream = IceCreamStand('Морозимся', flavor)
    print(IceCream)
    IceCream.print_flavors()
