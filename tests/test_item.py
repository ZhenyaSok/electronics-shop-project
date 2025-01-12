"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
from src.phone import Phone


import csv


item1 = Item("Смартфон", 10000, 20)


def test_string_to_number():
    assert Item.string_to_number("5.5") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    item2 = Item.all[0]
    assert item2.name == 'Смартфон'


def test_apply_discount():
    item3 = Item('Смарт-часы', 5000, 5)
    item3.apply_discount()
    assert 4000 * Item.pay_rate == 3400


def test_calculate_total_price():
    item3 = Item('Смарт-часы', 5000, 5)
    assert item3.calculate_total_price() == 25000

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

def test_str():
    item = Item('test1', 10000, 20)

def test_repr():
    """Проверка на ожидаемый результат по шаблону """
    item = Item('test1', 10000, 20)

    assert repr(item) == "Item('test1', 10000, 20)"


def test_instantiate_from_csv_error():
    error = Item.instantiate_from_csv('items.csv')
    assert error == 'Файл items.csv поврежден'

def test_instantiate_from_csv_error2():
    error = Item.instantiate_from_csv("random.csv")
    assert error == "Отсутствует файл item.csv"