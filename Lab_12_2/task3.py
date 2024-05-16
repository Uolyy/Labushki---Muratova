from Lab_12_2.task2 import IceCreamStand
from tkinter import Tk, Label, ttk, PhotoImage
from datetime import datetime


setattr(IceCreamStand, 'hours_is_open', (9, 21))


def is_open(self):
	now = datetime.now()
	open_hour, close_hour = self.hours_is_open
	open_time = open_hour <= now.hour < close_hour
	return 'открыто' if open_time else 'закрыто'


setattr(IceCreamStand, 'is_open', is_open)


def __str__(self):
	return (
		f'Название: {self.restaurant_name}\n'
		f'Часы работы: {self.working_hours} (сейчас {self.is_open()})\n'
		f'Расположение: {self.location}\n'
		f'Виды мороженого: {', '.join(self.icecream_types)}\n'
		f'Вкусы: {', '.join(self.flavors)}\n'
	)


setattr(IceCreamStand, '__str__', __str__)

my_icecream_stand = IceCreamStand(
		restaurant_name='Чилловые чашки',
		flavors=['Пьяная вишня', 'Шоколад-банан', 'Лимон-мята', 'Малина-мёд']
)


main_window = Tk()

main_window.title(my_icecream_stand.restaurant_name.upper())

main_window.geometry('600x700')
# Запрет на изменение размеров окна, так как это информационная панель и она должна иметь конкретные размеры,
# которые мы задали.
main_window.resizable(width=False, height=False)
# Иконка приложения слева вверху
main_window.iconbitmap('ice.ico')

main_window.attributes('-alpha', 0.9)

welcome_msg = ttk.Label(main_window, text=f'Добро пожаловать в {my_icecream_stand.restaurant_name}', font=("Arial", 10))

welcome_msg.pack()

my_logo = PhotoImage(file='ice.png')

logo_label = ttk.Label(main_window, image=my_logo)

logo_label.pack()

info_msg = ttk.Label(main_window, text=my_icecream_stand.__str__(), font=("Arial", 10))

info_msg.pack()


close_button = ttk.Button(main_window, text='Закрыть', command=main_window.destroy)
# Expand нужен, чтобы кнопка приклеилась к окну. А anchor='s' размещает ее в самом низу, по центру.
close_button.pack(expand=True, anchor='s')


def main():
	print(my_icecream_stand)
	main_window.mainloop()


if __name__ == '__main__':
	main()
