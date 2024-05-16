
from Lab_12_2.task1 import IceCreamStand

# 12.2) Модифицируйте ранее созданный IceCreamStand:
# 	1. Добавьте атрибуты для описания локации и времени работы кафе-мороженого
# 	2. Реализовать методы для добавления и удаления сортов мороженого из списка flavors
# 	3. Реализовать метод проверки наличия определенного сорта мороженого в списке flavors
# 	4. Добавить методы для разных типов мороженого (например, мороженое на палочке, мягкое мороженое и т.д)
# 	и реализовать методы для работы с каждым типом

setattr(IceCreamStand, 'working_hours', '9:00-21:00')
setattr(IceCreamStand, 'location', 'Энколово')
setattr(IceCreamStand, 'icecream_types', ['на палочке', 'мягкое', 'твердое', 'жидкое', 'вкусное'])
# Метод setattr позволяет добавлять новые атрибуты и методы уже существующему классу. Его минус состоит в том,
# что он не позволяет задавать значения по умолчанию, а добавляет их ровно так, как они заданы (третье значение в
# скобках). Поэтому, при использовании этого метода, нужно указывать значения явно.


def add_flavor(self, flavor: str):
	if not type(self.flavors) is list:
		self.flavors = []
	self.flavors.append(flavor)


def remove_flavor(self, flavor: str) -> None:
	self.flavors.remove(flavor)


def check_flavor(self, flavor: str) -> bool:
	return flavor in self.flavors


# Разумеется, не забыть присвоить классу наши новые методы, которые мы только что написали выше:
setattr(IceCreamStand, 'add_flavor', add_flavor)
setattr(IceCreamStand, 'remove_flavor', remove_flavor)
setattr(IceCreamStand, 'check_flavor', check_flavor)


def main() -> None:
	flavors = ['медовое']
	my_stand = IceCreamStand('Отбитые пчеловоды', flavors)
	my_stand.show_flavors()
	my_stand.add_flavor(input('Введите, какой вкус хотим добавить: '))
	my_stand.show_flavors()
	print(
			'Такой вкус есть'
			if my_stand.check_flavor(input('Введите, какой вкус хотим проверить: '))  # Если True
			else 'Такого нет'
	)


if __name__ == "__main__":
	main()
