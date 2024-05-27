import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6 import QtGui

from окно import Ui_MainWindow

from operator import add, sub, mul, truediv

operations = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.line_edit.maxLength()

        self.set_custom_cursor("лапка.png")

        # цифры
        self.ui.but_0.clicked.connect(self.add_num)
        self.ui.but_1.clicked.connect(self.add_num)
        self.ui.but_2.clicked.connect(self.add_num)
        self.ui.but_3.clicked.connect(self.add_num)
        self.ui.but_4.clicked.connect(self.add_num)
        self.ui.but_5.clicked.connect(self.add_num)
        self.ui.but_6.clicked.connect(self.add_num)
        self.ui.but_7.clicked.connect(self.add_num)
        self.ui.but_8.clicked.connect(self.add_num)
        self.ui.but_9.clicked.connect(self.add_num)

        # действия
        self.ui.but_clear.clicked.connect(self.clear_all)
        self.ui.but_ce.clicked.connect(self.clear_entry)
        self.ui.but_backspace.clicked.connect(self.backspace)

        self.ui.but_sign.clicked.connect(self.change_sign)

        # точка
        self.ui.but_tochka.clicked.connect(self.add_point)

        # операции
        self.ui.but_rez.clicked.connect(self.calculate)

        self.ui.but_plus.clicked.connect(self.math_operation)
        self.ui.but_min.clicked.connect(self.math_operation)
        self.ui.but_multi.clicked.connect(self.math_operation)
        self.ui.but_div.clicked.connect(self.math_operation)

    def add_num(self):  # добавление цифр
        self.temp_equality()
        self.remove_error()
        but = self.sender()  # Метод sender() возвращает Qt объект, который посылает сигнал; последняя нажатая кнопка

        number_but = ('but_0', 'but_1', 'but_2', 'but_3', 'but_4',
                      'but_5', 'but_6', 'but_7', 'but_8', 'but_9')

        if but.objectName() in number_but:
            if self.ui.line_edit.text() == '0':
                self.ui.line_edit.setText(but.text())
            else:
                self.ui.line_edit.setText(self.ui.line_edit.text() + but.text())

    def add_point(self) -> None:  # добавление точки, если её нет
        self.temp_equality()
        self.remove_error()
        if '.' not in self.ui.line_edit.text():
            self.ui.line_edit.setText(self.ui.line_edit.text() + '.')

    def clear_all(self) -> None:  # полная очистка
        self.ui.line_edit.setText('0')
        self.ui.label.clear()
        self.remove_error()

    def clear_entry(self) -> None:  # очистка поля ввода
        self.temp_equality()
        self.remove_error()
        self.ui.line_edit.setText('0')

    def backspace(self) -> None:  # удаление одного знака
        self.temp_equality()
        self.remove_error()
        entry = self.ui.line_edit.text()

        if len(entry) != 1:  # если 1 цифра или 1 цифра и минус, в строку вписывается 0, иначе удаляется последний знак
            if len(entry) == 2 and '-' in entry:
                self.ui.line_edit.setText('0')
            else:
                self.ui.line_edit.setText(entry[:-1])
        else:
            self.ui.line_edit.setText('0')

    @staticmethod  # декоратор
    def del_zeros(num: str) -> str:  # функция для незначащих нулей
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self) -> None:  # временное выражение сверху ввода
        btn = self.sender()
        entry = self.del_zeros(self.ui.line_edit.text())

        if not self.ui.label.text() or self.get_sign() == '=':
            self.ui.label.setText(entry + f' {btn.text()} ')
            self.ui.line_edit.setText('0')

    def get_entry_num(self):  # получения числа из поля ввода
        entry = self.ui.line_edit.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self):  # получение числа из временного выражения
        if self.ui.label.text():  # если в нём есть числа, разделяем по пробелам и берём первый элемент
            temp = self.ui.label.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_sign(self):  # получение знака из временного выражения
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def change_sign(self) -> None:  # смена знака числа
        self.temp_equality()
        self.remove_error()
        entry = self.ui.line_edit.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        # если число занимает всю возможную длину строки, то к длине прибавляется 1 и в строке добавляется -
        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.ui.line_edit.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.line_edit.setMaxLength(self.entry_max_len)

        self.ui.line_edit.setText(entry)

    def calculate(self):
        entry = self.ui.line_edit.text()
        temp = self.ui.label.text()

        try:
            if temp:
                result = self.del_zeros(
                    str(operations[self.get_sign()](self.get_temp_num(), self.get_entry_num()))
                )
                self.ui.label.setText(temp + self.del_zeros(entry) + ' =')
                self.ui.line_edit.setText(result)
                return result
        except KeyError:
            pass

        except ZeroDivisionError:
            self.ui.line_edit.setText('Ошибка')

    def math_operation(self) -> None:
        temp = self.ui.label.text()
        but = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_sign() != but.text():
                if self.get_sign() == '=':
                    self.add_temp()
                else:
                    self.ui.label.setText(temp[:-2] + f'{but.text()} ')
            else:
                self.ui.label.setText(self.calculate() + f' {but.text()}')

    def temp_equality(self) -> None:  # убирает = при вводе следующих чисел
        if self.get_sign() == '=':
            self.ui.label.clear()

    def remove_error(self) -> None:
        if self.ui.line_edit.text() == 'Ошибка':
            self.ui.line_edit.setText('0')

    def set_custom_cursor(self, cursor_image_path):
        pixmap = QtGui.QPixmap(cursor_image_path)
        cursor = QtGui.QCursor(pixmap)
        self.setCursor(cursor)  # Устанавливаем курсор для главного окна

        # Рекурсивно устанавливаем курсор для всех дочерних виджетов
        self.set_cursor_for_all_children(self, cursor)

    def set_cursor_for_all_children(self, widget, cursor):
        # Рекурсивно устанавливает курсор для всех дочерних виджетов.
        for child in widget.findChildren(QWidget):
            child.setCursor(cursor)
            self.set_cursor_for_all_children(child, cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
