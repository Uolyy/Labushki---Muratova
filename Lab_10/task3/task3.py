from icecream import ic
import os
from win10toast import ToastNotifier

en_ru_dict: dict = {}
with open('en-ru.txt', encoding='utf') as text_file:
	text_list = [translation.rstrip('\n') for translation in text_file]
	for line in text_list:
		key, value = line.split(' - ')
		en_ru_dict[key] = tuple(value.split(', '))
with open('ru-en.txt', 'w', encoding='utf') as text_file:
	ru_en_dict: dict = {value: key for key, value in en_ru_dict.items()}
	ru_en_dict = dict(sorted(ru_en_dict.items(), key=lambda item: item[0]))  # сортирует словарь по первому слову
	for key, value in ru_en_dict.items():
		print(f'{", ".join(key)} - {value}', file=text_file)


# По приколу, уведомление!
if os.path.exists('ru-en.txt'):
	toaster = ToastNotifier()
	toaster.show_toast(title='Ура!', msg='Словарь переведён', duration=2, threaded=True)
else:
	print('Даже не представляю, где тут еще можно было накосячить, но что-то опять пошло не так)')
