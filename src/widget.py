from masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(card_info: str) -> str:
    """Функция принимает информацию о счёте или карте и маскирует её"""

    card_type_list = []
    card_info_list = card_info.split()

    for string in card_info_list:
        if string.isalpha():
            card_type_list.append(string)

    card_type = " ".join(card_type_list)
    card_number = str(card_info_list[-1])

    if card_type == "Счет":
        return f"{card_type} {get_mask_account(card_number)}"

    return f"{card_type} {get_mask_card_number(card_number)}"


def get_data(data_info: str) -> str:
    """Функция корректного написания даты"""
    date_str = str(data_info)

    parsed_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = parsed_date.strftime("%d.%m.%Y")

    return formatted_date
