import os
import io
import requests
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
from tkinter import Tk, ttk, messagebox
from PIL import Image, ImageTk


def get_city() -> str:
	city = 'Сертолово'
	return city


def get_info(city: str) -> dict:
	API_KEY = os.getenv('API_KEY')
	search_result = requests.get(
			url='http://api.openweathermap.org/data/2.5/weather',
			params={
				'appid': API_KEY,
				'q': city,
				'units': 'metric',
				'lang': 'ru',
			}
	)
	search_result = search_result.json()
	pprint(search_result)
	if search_result['cod'] == '404':
		messagebox.showerror(title='Ошибка', message='Город не найден, проверьте правильность запроса')
	return search_result


def get_weather_params(search_result: dict) -> tuple:
	weather = search_result['weather'][0]['description']
	temperature = int(search_result['main']['temp'])
	temperature = '+' + str(temperature) if temperature > 0 else str(temperature)

	tempmin = int(search_result['main']['temp_min'])
	tempmin = '+' + str(tempmin) if tempmin > 0 else str(tempmin)

	tempmax = int(search_result['main']['temp_max'])
	tempmax = '+' + str(tempmax) if tempmax > 0 else str(tempmax)

	feels_like = int(search_result['main']['feels_like'])
	feels_like = '+' + str(feels_like) if feels_like > 0 else str(feels_like)

	wind = search_result['wind']['speed']

	timezone = int(search_result['timezone'])

	sunrise_ts = search_result['sys']['sunrise']
	sunrise = datetime.fromtimestamp(sunrise_ts + (timezone - 10800)).strftime('%H:%M:%S')

	sunset_ts = search_result['sys']['sunset']
	sunset = datetime.fromtimestamp(sunset_ts + (timezone - 10800)).strftime('%H:%M:%S')

	icon = search_result['weather'][0]['icon']
	icon_url = f'http://openweathermap.org/img/wn/{icon}@2x.png'

	return weather, temperature, tempmin, tempmax, feels_like, wind, sunrise, sunset, icon_url


def load_image(url):
	response = requests.get(url)
	image_data = response.content
	image = Image.open(io.BytesIO(image_data))
	photoimage = ImageTk.PhotoImage(image)

	return photoimage


def change_city(new_city: str, main_window: Tk) -> None:
	new_city = new_city.get()
	print('Ищу', new_city)
	city = new_city.title()
	if city == 'Петербург' or city == 'Petersburg':
		city = 'Санкт-Петербург'
	info = get_info(city)
	main_window.destroy()
	draw_main_window(city, info)


def check_env():
	dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
	if os.path.exists(dotenv_path):
		load_dotenv(dotenv_path)
	else:
		print(
				f'Не удалось найти файл.env в папке {os.path.dirname(__file__)}\n\n'
				f'Создайте файл.env в папке {os.path.dirname(__file__)} и добавьте в него константы API_KEY и чута еще'
		)
		exit()


def draw_main_window(city, info) -> None:
	weather, temperature, tempmin, tempmax, feels_like, wind, sunrise, sunset, icon_url = (
		get_weather_params(info))
	main_window = Tk()
	main_window.configure(background='gray')
	main_window.geometry('400x500')
	main_window.title(f'Прогноз погоды')
	main_window.attributes('-fullscreen', False, '-alpha', 0.9)
	main_text = ttk.Label(
			text=
			f'Погода в городе {city}\n\n'
			f'{weather.capitalize()}, температура {temperature}\n',
			font=('comic sans ms', 14, 'italic'),
	)
	main_text.configure(background='gray')
	main_text.pack()

	weather_image = load_image(icon_url)
	label_weather_image = ttk.Label(main_window, image=weather_image, borderwidth=50)
	label_weather_image.configure(background='gray', )
	label_weather_image.pack()

	frame = ttk.Frame(main_window)
	frame.pack(fill='both')
	weather_info_label = ttk.Label(
			frame,
			text=
			f'По ощущениям: {feels_like}\n'
			# f'В течение всего дня: от {tempmin} до {tempmax}\n'
			f'Ветер: {wind:.1f} м/с\n'
			f'Время восхода: {sunrise}. Время заката: {sunset}\n',
			font=('arial', 11, 'italic')
	)
	weather_info_label.pack()

	entry = ttk.Entry(main_window, takefocus=True, width=30)
	entry.pack(expand=True)
	entry.bind('<Return>', lambda event: change_city(entry, main_window))

	search_button = ttk.Button(main_window, text='Поиск', command=lambda: change_city(entry, main_window))
	search_button.pack()

	close_button = ttk.Button(text='Закрыть', command=main_window.destroy)
	close_button.pack(expand=True, fill='x')
	main_window.mainloop()


def main() -> None:
	check_env()
	city = get_city()
	info = get_info(city)
	draw_main_window(city, info)


if __name__ == '__main__':
	main()
