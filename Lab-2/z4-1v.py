# 2.4 - 1 версия)
# красный и синий - фиолетовый;
# красный и желтый - оранжевый;
# синий и желтый - зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

# Решение №1 только с помощью if ... elif ... else

color1 = int(input("Введите номер первого цвета: 1 - красный; 2 - синий; 3- желтый: "))
color2 = int(input("Введите номер второго цвета: 1 - красный; 2 - синий; 3- желтый: "))

if color1 in range(1, 4) and color2 in range(1, 4):
    if color1 == 1:
        if color2 == 1:
            print("Получится красный цвет")
        if color2 == 2:
            print("Получится фиолетовый цвет")
        if color2 == 3:
            print("Получится оранжевый цвет")
    elif color1 == 2:
        if color2 == 1:
            print("Получится фиолетовый цвет")
        if color2 == 2:
            print("Получится синий цвет")
        if color2 == 3:
            print("Получится зеленый цвет")
    elif color1 == 3:
        if color2 == 1:
            print("Получится оранжевый цвет")
        if color2 == 2:
            print("Получится зеленый цвет")
        if color2 == 3:
            print("Получится желтый цвет")
else:
    print("Ошибка")