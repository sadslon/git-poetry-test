def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты и отправляет маску согласно правилу"""

    card_number_str = str(card_number)

    mask_number = f"{card_number_str[:4]} {card_number_str[4:6]} ** **** {card_number_str[12:]}"
    return mask_number


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: int) -> str:
    """Функция принимает номер счета в виде числа и возвращает маску номера по правилу"""
    account_number_str = str(account_number)

    mask_account = f"**{account_number_str[-4:]}"
    return mask_account


if __name__ == "__main__":
    print(get_mask_account(73654108430135874305))
