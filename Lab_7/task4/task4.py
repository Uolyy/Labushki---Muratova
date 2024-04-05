from Lab_7.functions import check_output, find_image
from PIL import Image

images: str | list | None = find_image()
if images:
    check_output()
    if type(images) is str:
        images = list(images)
    for image in images:
        with Image.open(image) as im:
            wm = Image.open('wm/watermark.png')
            wm.thumbnail((100, 100))
            position = (im.width // 2), (im.height // 2)
            im.paste(wm, position, mask=wm)
            im.save('output/' + 'watermarked_' + image)
            wm.close()

else:
    print('Файл не найден')

# 7.4)	Напишите программу, которая добавляет на изображение водяной знак.
# Можно тоже применять сразу к нескольким изображениям.
