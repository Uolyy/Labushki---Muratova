from PIL import Image

# 8.2)	Создайте словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему».
# Спросите у пользователя, к какому празднику ему нужна открытка и выведите нужную открытку на экран.

holidays: dict[str: str] = {
    'С днем эмалированного бидона': 'postcards/bidon.png',
    'С днем сыра-косички': 'postcards/cheese.png',
    'С днем диоксида кремния': 'postcards/dioksid.png',
    'С днем синей изоленты': 'postcards/izolenta.png',
    'С международным днем паники': 'postcards/panika.png',
    'С днем плиты': 'postcards/plita.png',
    'С днем кафельной плитки': 'postcards/plitka.png',
    'С днем рождения кота!': 'postcards/drkota.png',
    'С днём жабьего срединства!': 'postcards/wednesday.png'
}


def main() -> None:
    holidays_list = list(holidays.keys())  # Список праздников, чтобы к ключам словаря можно было обращаться по индексу
    print('Список праздников:')
    for index, holiday in enumerate(holidays_list, start=1):
        # Перебор индексов вместе с содержимым словаря
        print(
            f'{index} — {holiday:.>30}'  # индекс – праздник, выравнивание по правому краю
        )

    user_choice: int = int(input('\nВведите номер праздника: ')) - 1
    postcard_path: str = holidays.get(holidays_list[user_choice])
    # Получение значения словаря holidays по ключу, взятому из словаря holidays_list

    with Image.open(postcard_path) as postcard:
        postcard.show()


if __name__ == '__main__':
    main()
