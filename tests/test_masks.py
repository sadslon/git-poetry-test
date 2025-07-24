import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number", [
    '22202345612340099',  # слишком длинный номер
    '1234',  # слишком короткий номер
    '1234 5678',  # содержит пробелы
    'abc123',  # содержит буквы
])
def test_get_mask_card_number_invalid(card_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == "Введите номер карты в виде строки, состоящий из 16 цифр без пробелов"


@pytest.fixture
def card_numbers():
    return [
        "7000876789784565",  # длинный валидный номер
        "1234567812345678",  # другой валидный номер
    ]


def test_get_mask_card_number(card_numbers):
    expected = [
        "7000 87 ** **** 4565",
        "1234 56 ** **** 5678",
    ]
    for card_number, expected_mask in zip(card_numbers, expected):
        assert get_mask_card_number(card_number) == expected_mask


@pytest.fixture
def account_numbers():
    return [
        "12345678901234567890",  # стандартный номер счета
        "12345",                 # короткий номер
        "123",                   # еще более короткий
        "invalid_format",        # неправильный формат
    ]

def test_get_mask_account(account_numbers):
    expected = [
        "**7890",               # валидный номер
        "Номер счета слишком короткий",  # короткий номер
        "Номер счета слишком короткий"   # еще более короткий номер
    ]

    # Тестирование валидного номера счета
    assert get_mask_account(account_numbers[0]) == expected[0]
    # Тестирование еще более короткого номера счета
    assert get_mask_account(account_numbers[2]) == expected[2]
    # Тестирование неправильного формата
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_numbers[3])
    assert str(exc_info.value) == "Введите номер счета в виде строки, состоящий из цифр"