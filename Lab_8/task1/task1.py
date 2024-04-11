from PIL import Image
from Lab_7.functions import check_output, get_image_name


# 8.1)	Скачайте любую открытку из интернета, определите область,
# которую Вам нужно вырезать из данного изображения (обрезать текст, часть фото и т.д.).
# Напишите программу, которая выполнит эту операцию. Сохраните изображения в текущую папку под новым именем.

def main() -> None:
    image_name: str | None = get_image_name()
    if image_name:
        check_output()
        with Image.open(image_name) as postcard:
            postcard_cropped = postcard.crop((215, 30, 633, 450))  # postcard.size: (640, 480)
            #  x, y верхнего левого угла, x, y нижнего правого угла – кортеж
            postcard_cropped.save('output/' + 'cropped_' + image_name)

    else:
        print('Файл не найден')


if __name__ == "__main__":
    main()
