from PIL import Image
from Lab_7.functions import get_image_name, check_output


# 7.2)	Напишите программу, которая создаёт уменьшенную в три раза копию изображения.
# Получите горизонтальный и вертикальный зеркальный образ изображения.
# Сохраните изображения в текущую папку под новым именем.


def main() -> None:
    image_name: str | None = get_image_name()
    if image_name:
        check_output()
        with Image.open(image_name) as im:
            im.transpose(Image.FLIP_LEFT_RIGHT).save('output/' + 'hor-reversed-' + image_name)
            im.transpose(Image.FLIP_TOP_BOTTOM).save('output/' + 'ver-reversed-' + image_name)
            width, height = im.size
            im.thumbnail((width // 3, height // 3))
            im.save('output/' + 'reduced-' + image_name)
    else:
        print('Файл не найден')
