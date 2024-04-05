import os


# Функция, которая ищет изображения в текущей директории
def find_image() -> list | None:
    file_names: list = []
    extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.ico']  # Список возможных расширений файлов
    for file in os.listdir():  # цикл по текущей директории
        for extension in extensions:
            # если file - файл, оканчивающийся на одно из расширений из списка
            if os.path.isfile(file) and file.endswith(extension):  # проверка на файл, ибо и папка может стать png >.<
                file_names.append(file)
    return file_names if file_names else None  # Возвращает список файлов, если они есть (if ... == True), иначе ничего


def get_image_name() -> str:
    """
    Функция, которая ищет изображения. Если их несколько, позволяет выбрать нужное.
    :return: Возвращает название изображения строкой
    """
    images = find_image()
    if images:  # если есть изображения: ...
        if len(images) == 1:
            return images[0]
        else:
            # генератор словаря, enumerate – здесь цикл, перебирающий значения и индексы
            images_dict: dict = {key: value for key, value in enumerate(images, start=1)}
            print('Найдены изображения:\n')
            for key, value in images_dict.items():
                print(f'{key} - {value}')
            return images_dict.get(int(input('Введите номер изображения: ')))  # get возвращает значение словаря


def check_output() -> None:
    if not os.path.exists('output'):
        os.makedirs('output')
