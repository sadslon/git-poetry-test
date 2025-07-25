def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и отправляет маску согласно правилу"""

    # Проверка на корректный ввод
    if not isinstance(card_number, str) or not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Введите номер карты в виде строки, состоящий из 16 цифр без пробелов")

    mask_number = f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"
    return mask_number


# Проверка работы кода
if __name__ == "__main__":
    print(get_mask_card_number("7000876789784565"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета в виде строки и возвращает маску номера по правилу"""

    # Проверка на корректный ввод
    if not isinstance(account_number, str) or not account_number.isdigit():
        raise ValueError("Введите номер счета в виде строки, состоящий из цифр")

    if len(account_number) < 4:
        return "Номер счета слишком короткий"

    mask_account = f"**{account_number[-4:]}"
    return mask_account


# Проверка работы кода
if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))