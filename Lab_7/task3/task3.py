from PIL import Image, ImageFilter
from Lab_7.functions import find_image, check_output


# 7.3)	Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg.
# Напишите программу, которая применит ко всем этим файлам сразу любой фильтр
# (кроме размытия, т.к. он рассматривался на лекции). Сохраните изображения в новую папку под новыми именами.


images: list = find_image()

if not type(images) is list:
    print('Для задачи необходимо подготовить пять графических файлов')
    exit()
check_output()
for image in images:
    with Image.open(image) as im:
        im.filter(ImageFilter.EMBOSS).save('output/' + 'filtered_' + image)
