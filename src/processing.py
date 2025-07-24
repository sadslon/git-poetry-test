from datetime import datetime


def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """Функция возвращает новый список словарей у которых ключ state соответствует указанному значению"""

    new_filtered_list = []

    for dict_item in list_of_dict:
        if dict_item.get("state") == state:
            new_filtered_list.append(dict_item)

    return new_filtered_list


# Проверка работы кода
if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )


def sort_by_date(data):
    """Сортирует список словарей по дате в порядке возрастания."""

    sorted_data = sorted(data, key=lambda x: x['date'])
    # Преобразуем дату в строку формата 'YYYY-MM-DD'
    for item in sorted_data:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    return sorted_data


# Проверка работы кода
if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
