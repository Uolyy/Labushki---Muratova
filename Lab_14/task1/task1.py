import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from convert import Ui_MainWindow
from dotenv import load_dotenv
import os

# Загрузить переменные окружения из файла .env
load_dotenv()
API_KEY = os.getenv('API_KEY')


# Получаем курс валюты
def get_exchange_rate(from_currency, to_currency):
	url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}'
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		return data['conversion_rates'][to_currency]
	else:
		return None


class Converter(QMainWindow):
	def __init__(self):
		super(Converter, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setup_connections()

	def setup_connections(self):
		self.ui.btn_rub_out.clicked.connect(lambda: self.convert_currency('RUB'))
		self.ui.btn_usd_out.clicked.connect(lambda: self.convert_currency('USD'))
		self.ui.btn_eur_out.clicked.connect(lambda: self.convert_currency('EUR'))

	def convert_currency(self, to_currency):
		from_currency = self.get_selected_currency()
		if from_currency is None:
			QMessageBox.warning(self, "Ошибка", "Выберите валюту для конвертации")
			return

		amount = self.ui.line_in.text()
		if not amount.isdigit():  # проверяет, что введенная строка содержит только цифры
			QMessageBox.warning(self, "Ошибка", "Введите корректную сумму для конвертации")
			return

		amount = float(amount)
		rate = get_exchange_rate(from_currency, to_currency)
		if rate is None:
			QMessageBox.warning(self, "Ошибка", "Не удалось получить курс валют")
			return

		result = amount * rate
		self.ui.line_out.setText(f"{result:.2f}")

	def get_selected_currency(self):
		if self.ui.btn_rub_in.isChecked():
			return 'RUB'
		elif self.ui.btn_usd_in.isChecked():
			return 'USD'
		elif self.ui.btn_eur_in.isChecked():
			return 'EUR'
		return None


if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = Converter()
	window.show()

	sys.exit(app.exec())
