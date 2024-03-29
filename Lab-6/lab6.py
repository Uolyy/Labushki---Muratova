from icecream import ic


# 6.1)	Создайте словарь, содержащий перечень стран и их столиц.
# a)	Выведите на экран все пары ключ-значение.
# b)	Выведите на экран столицу для определенной страны.
# c)	Отсортируйте и выведите на экран содержимое словаря в алфавитном порядке названий стран.
def task_1():
    countries = {'Россия': 'Москва', 'Испания': 'Мадрид', 'Австралия': 'Канберра', 'Лапландия': 'Рованиеми'}
    print("Список стран и их столиц: ")
    for key, value in countries.items():
        print(f"{key}: {value}")

    country = input("\nВведите страну: ")
    if country.title() in countries:
        print(f"Столица данной страны: {countries[country.title()]}\n")
    else:
        print("Такой страны нет в нашем словаре :<\n")

    list_countries = list(countries.keys())
    list_countries.sort()
    print("Список стран в алфавитном порядке: ")
    for i in list_countries:
        print(i, ':', countries[i])


# task_1()


# 6.2)	В игре в слова «Эрудит» каждая буква имеет определенную ценность:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
def task_2():
    erudite = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
               3: ['Б', 'Г', 'Ё', 'Ь', 'Я'], 4: ['Й', 'Ы'], 5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
               8: ['Ш', 'Э', 'Ю'], 9: ['Ф', 'Щ', 'Ъ']
               }
    word = input("Введите любое слово: ").upper()
    score = 0
    for letter in word:
        for key, letters in erudite.items():
            if letter in letters:
                score += key
                break
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


task_3()
