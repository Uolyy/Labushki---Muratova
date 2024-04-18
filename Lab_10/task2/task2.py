import json
from Lab_10.task1.task1 import main as read_json

# 10.2) Модифицируйте программу 10.1 – добавьте в нее код,
# который добавляет данные в файл JSON (спрашивает их у пользователя)
# и потом также выводить содержимое итогового файла на экран.


def json_add_value() -> None:
	with open('prod.json', 'r', encoding='utf') as json_file:
		products_data: dict = json.load(json_file)
		print('Что хотите добавить в список? \n')
		products_data['products'].append({
			'name': input('Введите название продукта: '),
			'price': int(input('Введите цену: ')),
			'weight': int(input('Введите вес: ')),
			'available': True if input('Товар доступен? (Да/Нет): ').lower() == 'да' else False})
	with open('prod.json', 'w', encoding='utf') as json_file:
		# dump записывает словарь в json файл (обратно load)
		json.dump(products_data, json_file, ensure_ascii=False, indent=4)


def main() -> None:
	json_add_value()
	read_json()


if __name__ == '__main__':
	main()
