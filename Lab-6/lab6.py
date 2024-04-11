from icecream import ic


# 6.1)	Создайте словарь, содержащий перечень стран и их столиц.
# a)	Выведите на экран все пары ключ-значение.
# b)	Выведите на экран столицу для определенной страны.
# c)	Отсортируйте и выведите на экран содержимое словаря в алфавитном порядке названий стран.
def task_1():
    countries = {
        'Россия': 'Москва',
        'Испания': 'Мадрид',
        'Австралия': 'Канберра',
        'Лапландия': 'Рованиеми'
    }
    print("Список стран и их столиц: ")
    for key, value in countries.items():
        print(f"{key}: {value}")

    # генерирует инвертированный словарь – столица: страна
    inv_countries: dict = {capital: country for country, capital in countries.items()}

    my_input = input("\nВведите страну или город: ").title()
    # конструкция get(key, default) – если такого ключа в словаре нет - выполняется default
    print(countries.get(my_input, inv_countries.get(my_input, 'Такого города или страны нет в нашем словаре')))

    list_countries = list(countries.keys())
    list_countries.sort()
    print("\nСписок стран в алфавитном порядке: ")
    for i in list_countries:
        print(i, ':', countries[i])


task_1()


# 6.2)	В игре в слова «Эрудит» каждая буква имеет определенную ценность:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
def task_2():
    erudite = {
        1: 'авеинорст',
        2: 'дклмпу',
        3: 'бгёья',
        4: 'йы',
        5: 'жзхцч',
        8: 'шэю',
        9: 'фщъ'
    }
    word = input("Введите любое слово: ").lower()
    score = 0
    for letter in word:
        for key in erudite:
            if letter in erudite[key]:
                score += key
    print(f"Стоимость слова {word} — {score}")


# task_2()


# 6.3)	*Доп.задание на множество.
# Есть множество студентов. Каждый из них знает некоторое количество языков.
# Нужно определить сколько различных языков знают студенты.
# Выведите отсортированный список этих языков. Выведите список студентов, которые знают китайский язык.
ic.disable()


def task_3():
    students: dict = {
        'student1': {'китайский', 'английский', 'французский', 'русский'},
        'student2': {'английский', 'русский'},
        'student3': {'испанский', 'французский', 'немецкий'},
        'student4': {'русский', 'английский', 'китайский', 'японский'},
        'student5': {'шотландский', 'китайский', 'шведский'},
        'student6': {'русский', 'немецкий', 'испанский'}
    }
    languages: set = set()
    for language in students.values():
        ic(language)
        languages.update(language)

    sorted_languages: list = sorted(languages)
    print(f"Список всех языков, которые знают студенты:\n{', '.join(sorted_languages)}")

    chinese_speaker: set = set()
    for student, language in students.items():
        if "китайский" in language:
            chinese_speaker.add(student)
    print(f"Китайский язык знают: {', '.join(chinese_speaker)}")

# task_3()
