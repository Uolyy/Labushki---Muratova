from Lab_8.task1.task1 import main as get_cropped_image
import os
from icecream import ic
from PIL import Image, ImageDraw, ImageFont
import random
from time import sleep

# 8.3)	Модифицируйте задачу 8.1 так: спросите еще у пользователя, имя того, кого он хочет поздравить,
# добавьте на заданную открытку текст «…, поздравляю!», где вместо … вставьте полученное имя
# (выведите его разным цветом и шрифтами, посередине вверху или внизу фото).
# Найдите в сети интернет решение, как сделать надпись жирным текстом (по умолчанию, такого параметра нет).
# Сохраните новую открытку в файл с расширением png.


ic.disable()
placement: dict = {
    'вверху': (25, 20),
    'по центру': (180, 200),
    'внизу': (205, 335),
    'случайно': (random.randint(25, 205), random.randint(20, 330))
}

fonts: dict = {
    'Comic Sans MS': 'comic.ttf',
    'Comic Sans MS жирный': 'comicbd.ttf',
    'Calibri': 'calibri.ttf',
    'Calibri жирный': 'calibrib.ttf',
    'Candara': 'Candara.ttf',
    'Candara жирный': 'Candarab.ttf',
    'Candara жирный курсив (пушка, бомба)': 'Candaraz.ttf',
}

# либо сделать выбор пользователем, жирный шрифт или обычный
# в конце: stroke_width=1 или stroke_width=0
# bold = int(input("Жирный шрифт – 1\n Обычный шрифт – 0"))   + проверки

colors: dict = {
    'черный': (0, 0, 0),
    'красный': (255, 0, 0),
    'зеленый': (0, 255, 0),
    'синий': (0, 0, 255),
    'желтый': (255, 255, 0),
    'бирюзовый': (0, 255, 255),
    'малиновый': (255, 0, 255),
}


def pick_position(switch_error: bool = False) -> tuple:
    """
    :param switch_error: По умолчанию False, если вводится неверное числовое значение, функция перезапускается с
    параметром True
    :return: возвращает кортеж с координатами надписи в функцию draw_text
    """
    if switch_error:
        print(
            'Вы ввели неправильное значение. Попробуйте еще раз.\n\n'
        )
        sleep(1)

    places: list = [place for place in placement.keys()]
    ic(places)
    print('\nГде разместить надпись?')
    for number, place in enumerate(places, start=1):
        print(f'{number} — {place}')
    try:
        choice = int(input('Введите номер: '))
        return placement.get(places[choice - 1]) if 0 < choice <= len(places) else pick_position(True)
    except Exception as e:
        ic(e)
        return pick_position(True)


def pick_font(switch_error: bool = False) -> str:
    if switch_error:
        print(
            'Вы ввели неправильное значение. Попробуйте еще раз.\n\n'
        )
        sleep(1)
    fonts_list: list = [font for font in fonts.keys()]
    ic(fonts_list)
    print('\nКакой выберем цвет?')
    for number, font in enumerate(fonts_list, start=1):
        print(f'{number} — {font}')
    try:
        choice = int(input('Введите номер: '))
        return fonts.get(fonts_list[choice - 1]) if 0 < choice <= len(fonts_list) else pick_font(True)
    except Exception as e:
        ic(e)
        return pick_font(True)


def pick_color(switch_error: bool = False) -> tuple:
    if switch_error:
        print(
            'Вы ввели неправильное значение. Попробуйте еще раз.\n\n'
        )
        sleep(1)
    colors_list: list = [color for color in colors.keys()]
    ic(colors_list)
    print('\nКакой выберем шрифт?')
    for number, color in enumerate(colors_list, start=1):
        print(f'{number} — {color}')
    try:
        choice = int(input('Введите номер: '))
        return colors.get(colors_list[choice - 1]) if 0 < choice <= len(colors_list) else pick_color(True)
    except Exception as e:
        ic(e)
        return pick_color(True)


def get_fonts_path():
    return os.path.join(os.environ['SystemRoot'], 'Fonts')  # смотрит, где находится системная папка со шрифтами


def draw_text(image_name: str, name: str, position: tuple, font: str, color: tuple):
    with Image.open('output/' + image_name) as postcard:
        ic(postcard.size)
        greeting = ImageDraw.Draw(postcard)
        greeting.text(
            xy=position,
            text=f'{name}!\nПоздравляю!',
            # stroke_width=bold,
            fill=color,
            font=font
        )
        postcard.show()


def main() -> None:
    get_cropped_image()
    if os.listdir('output') and len(os.listdir('output')) == 1:
        image_name = os.listdir('output')[0]
        name = input('Кого хотите поздравить?: ')
        position = pick_position()
        font_path = get_fonts_path() + '/' + pick_font()
        font = ImageFont.truetype(font=font_path, size=30)
        color = pick_color()
        draw_text(image_name, name, position, font, color)
    else:
        print('Что-то пошло не так, попробуйте снова')


if __name__ == "__main__":
    main()
