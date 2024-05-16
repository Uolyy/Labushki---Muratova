import requests
import random
from tkinter import PhotoImage
from Lab_13.task1.task1 import load_image as process_image_from_url
from pprint import pprint
from icecream import ic
from customtkinter import CTk, set_appearance_mode, CTkButton


def get_cat_url() -> str:
	ic()
	result = requests.get("https://cataas.com/cat?json=true")
	ic(result.status_code)
	if result.status_code == 200:
		data = result.json()
	else:
		raise Exception("Не удалось получить данные")
	pprint(data)
	print(f'https://cataas.com/cat/{data["_id"]}')
	cat_url = f'https://cataas.com/cat/{data["_id"]}'
	return cat_url


def get_dog_url() -> str:
	ic()
	result = requests.get("https://dog.ceo/api/breeds/image/random")
	ic(result.status_code)
	if result.status_code == 200:
		data = result.json()
	else:
		raise Exception("Не удалось получить данные")
	pprint(data)
	dog_url = data["message"]
	return dog_url


def get_duck_url() -> str:
	ic()
	result = requests.get('https://random-d.uk/api/v2/random')
	ic(result.status_code)
	if result.status_code == 200:
		data = result.json()
	else:
		raise Exception("Не удалось получить данные")
	pprint(data)
	duck_url = data["url"]
	return duck_url


def get_fox_url() -> str:
	ic()
	result = requests.get('https://randomfox.ca/floof')
	ic(result.status_code)
	if result.status_code == 200:
		data = result.json()
	else:
		raise Exception("Не удалось получить данные")
	pprint(data)
	fox_url = data["image"]
	return fox_url


animals: dict = {
	"cat": get_cat_url,
	"dog": get_dog_url,
	"duck": get_duck_url,
	"fox": get_fox_url,
}


def get_random_image(big_button) -> None:
	animal_choice = random.choice(list(animals.keys()))
	choosen_url = animals[animal_choice]()
	ic(choosen_url)
	image = process_image_from_url(choosen_url)
	big_button.configure(image=image)


def draw_gui(app: CTk, image: PhotoImage = None) -> None:
	app.title("Рандомные животинки")
	app.attributes("-fullscreen", False)
	set_appearance_mode("dark")
	ic(image)
	image = process_image_from_url(
			'https://images.dog.ceo/breeds/retriever-golden/n02099601_8005.jpg') if image is None else image
	print('изображение', image)
	big_button = CTkButton(master=app, text='Жми сюда', command=lambda: get_random_image(big_button), image=image)
	big_button.pack()
	close_button = CTkButton(master=app, text='Закрыть', command=app.destroy)
	close_button.pack(fill='x', expand=True)

	app.mainloop()


def main() -> None:
	app = CTk()
	draw_gui(app)


if __name__ == "__main__":
	main()
