from Lab_11.task1.task1 import Restaurant

# 12.1) На основе ранее созданного класса Restaurant из прошлого задания создайте разновидность
# ресторана – «Кафе-мороженое». Напишите класс IceCreamStand, наследующий от класса Restaurant.
# Добавьте атрибут с именем flavors для хранения списка сортов мороженого. Напишите метод,
# который выводит этот список. Создайте экземпляр IceCreamStand и вызовите метод.

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, flavors, cuisine_type: str = 'Мороженое'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors: list = flavors

	def __str__(self):
		return (
			f'Название: {self.restaurant_name}\n'
			f'Вкусы: {self.flavors}'
		)

	def show_flavors(self):
		print(f'Вкусы: {', '.join(self.flavors)}')


flavors = ['Шоколад-банан', 'Лимон-мята', 'Малина-мёд']

ice_cream_stand = IceCreamStand(
		restaurant_name='Морозимся',
		flavors=flavors
)


def main() -> None:
	print(f'Привет, с вами кафе-мороженое {ice_cream_stand.restaurant_name}!\n')
	ice_cream_stand.show_flavors()


if __name__ == '__main__':
	main()
