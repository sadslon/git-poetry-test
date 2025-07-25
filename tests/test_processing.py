from datetime import datetime

import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def data():
    return [
        {"id": 1, "state": "active", "date": "2022-01-01"},
        {"id": 2, "state": "inactive", "date": "2021-01-01"},
        {"id": 3, "state": "active", "date": "2023-01-01"},
    ]


def test_filter_by_state(data):
    assert filter_by_state(data, "active") == [
        {"id": 1, "state": "active", "date": "2022-01-01"},
        {"id": 3, "state": "active", "date": "2023-01-01"},
    ]
    assert filter_by_state(data, "inactive") == [
        {"id": 2, "state": "inactive", "date": "2021-01-01"},
    ]
    assert filter_by_state(data, "nonexistent") == []


@pytest.mark.parametrize("data, expected", [
    ([
        {'date': datetime(2023, 1, 1), 'id': 0},
        {'date': datetime(2022, 1, 1), 'id': 2}
    ], [
        {'date': '2022-01-01', 'id': 2},
        {'date': '2023-01-01', 'id': 0}
    ]),
])
def test_sort_by_date(data, expected):
    assert sort_by_date(data) == expected