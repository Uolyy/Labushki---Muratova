import random


# 5.1)	Создайте список из пяти любых чисел.
# Спросите у пользователя число.
# Проверьте, есть ли данное число в списке.
# Выведите исходный список, число пользователя и соответствующие сообщение
# ("Поздравляю, Вы угадали число!" или "Нет такого числа!").
def task_1():
    numbers = [random.randint(1, 50) for _ in range(5)]
    num = int(input("Введите любое число: "))
    print(f"Исходный список: {numbers} \nВаше число: {num}")
    if num in numbers:
        print("Поздравляю, Вы угадали число! ")
    else:
        print("Такого числа нет :<")


# task_1()


# 5.2)	Создайте любой список. Определите, есть ли в списке повторяющиеся элементы,
# если да, то вывести на экран это значение.
def task_2():
    arr = []
    for i in range(15):
        num = random.randint(1, 50)
        arr.append(num)

    new_arr = []
    for i in arr:
        if arr.count(i) > 1 and i not in new_arr:
            new_arr.append(i)

    print(
        f"Список: {arr}\n"
        f"Количество повторяющихся элементов: {len(new_arr)}\n"
        f"Элементы: {new_arr}"
    )


# task_2()


# 5.3)	Задан кортеж с перечнем названий дней недели.
# Спросить у пользователя, сколько выходных на неделе он хочет и вывести два списка:
# "Ваши выходные дни: ..." - перечислить здесь столько дней недели с конца кортежа, сколько введено пользователем.
# "Ваши рабочие дни: ..." - перечислить здесь оставшиеся дни недели.
def task_3():
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    rest = int(input("Введите, сколько выходных на недели Вы хотите: "))
    print(
        f"Ваши выходные дни: {', '.join(days[-rest:])}\n"
        f"Ваши рабочие дни: {', '.join(days[:-rest])}"
    )


# task_3()


# 5.4)	Создайте два списка: один из 10 фамилий студентов Вашей группы, другой из 10 фамилий студентов другой группы.
# a.	Создайте спортивную команду (объедините в один кортеж) по 5 любых студентов из каждой группы.
# b.	Выведите на экран исходные списки групп и новый полученный кортеж.
# c.	Выведите его длину.
# d.	Отсортируйте кортеж по алфавиту.
# e.	Определите, входит ли в полученную команду студент "Иванов". И сколько раз встречается эта фамилия в кортеже.
def task_4():
    stud_1 = ['Иванов', 'НеИванов', 'Иванов', 'Карасиков', 'Кот', 'Миронова', 'Петров', 'Сидоров', 'Медведев', 'Чай']
    stud_2 = [
        'Зотова', 'Бережная', 'Ахмедова', 'Иванов', 'Кузнецова', 'Попова', 'Денисова', 'Алиева', 'Коробова', 'Ескина']
    stud_sport = random.sample(stud_1, 5) + random.sample(stud_2, 5)
    print(
        f"Первая группа: {', '.join(stud_1)}\n"
        f"Вторая группа: {', '.join(stud_2)}\n\n"
        f"Спортивная команда: {', '.join(stud_sport)}\n"
        f"Количество человек в спортивной команде: {len(stud_sport)}"
    )

    stud_sport2 = sorted(stud_sport)
    print(f"Спортивная команда в алфавитном порядке: {', '.join(stud_sport2)}")

    if 'Иванов' in stud_sport:
        if stud_sport.count('Иванов') == 1:
            print(f"В команде есть один студент Иванов")
        else:
            print(f"В команде несколько Ивановых: {stud_sport.count('Иванов')} ")
    else:
        print("В команде нет студента с фамилией Иванов")

# task_4()
