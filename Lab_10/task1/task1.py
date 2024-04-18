import json
from pprint import pprint


def main() -> None:
	with open('prod.json', encoding='utf') as json_file:
		products_data = json.load(json_file)  # load считывает json файл и превращает его в словарь
		pprint(products_data, indent=3, sort_dicts=False)
		for product in products_data['products']:
			print(
					f'Название: {product["name"]}\n'
					f'Цена: {product["price"]}\n'
					f'Вес: {product["weight"]}\n'
					f'{"В наличии" if product["available"] else "Нет в наличии!"}\n'
			)


if __name__ == '__main__':
	main()
