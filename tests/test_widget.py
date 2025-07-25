import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize('account_card, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83 ** **** 5199'),  # пример форматирования
    ('Счет 64686473678894779589', 'Счет **9589'),  # форматирование счета
    ('MasterCard 7158300734726758', 'MasterCard 7158 30 ** **** 6758'),  # форматирование карты
    ('Счет 35383033474447895560', 'Счет **5560'),  # форматирование нормального номера счета
    ('', 'Invalid input'),  # пустой ввод
    ('123', 'Invalid input'),  # некорректный тип данных
    ('Invalid Account/12345', 'Invalid input'),  # некорректный ввод
])
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_mask_account_card_invalid():
    assert mask_account_card('123') == "Invalid input"  # некорректный тип данных
