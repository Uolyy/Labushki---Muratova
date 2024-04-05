from PIL import Image
from Lab_7.functions import get_image_name

# 7.1)	Подготовьте любой графический файл для выполнения практической работы.
# Напишите программу, которая открывает и выводит этот файл на экран.
# Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.

# image = Image.open('бобр.png')
# image.show()
# print(f"Размер изображения: {image.size}\n"
#       f"Цветовая модель: {image.mode}\n"
#       f"Формат: {image.format}")

image_name: str | None = get_image_name()
if image_name:
    with Image.open(image_name) as im:		# with .open - чтобы не закрывать самому файл, ибо кому оно надо
        width, height = im.size     # size возвращает кортеж - ширину и высоту
        print(
            f'Название файла:\n {image_name:-^25}\n'
            f'Размер изображения: \n'
            f'{" ":<20}Ширина: {width} \n'
            f'{" ":<20}Высота: {height} \n'
            f'Формат файла: {im.format} \n'
            f'Цветовая модель: {im.mode} \n'
        )

        if (answer := input('Просмотреть изображение? Да/Нет: ')) in ('Д', 'д', 'Да', 'да'):
            im.show()
        elif answer in ('Н', 'н', 'Нет', 'нет'):
            exit()
        else:
            print('Вы ввели какую-то фигню, я так больше не могу')
            exit()
else:
    print('Файл не найден')
