"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_apply_discount():
    item3 = Item('Смарт-часы', 5000, 5)
    item3.apply_discount()
    assert 4000 * Item.pay_rate == 3400


def test_calculate_total_price():
    item3 = Item('Смарт-часы', 5000, 5)
    assert item3.calculate_total_price() == 25000

