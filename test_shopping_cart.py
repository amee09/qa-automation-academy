import pytest
from shopping_cart import calculate_total


def test_calculate_total():
    result = calculate_total(20, 3)
    assert result == 60


def test_zero_quantity():
    result = calculate_total(20, 0)
    assert result == 0


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total(20, -2)