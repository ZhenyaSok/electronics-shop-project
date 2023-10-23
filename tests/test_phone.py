from src.phone import Phone
from src.item import Item
def test_repr():
    """Проверка на ожидаемый результат по шаблону """
    phone = Phone('iPhone_apple', 100000, 20, 5)
    assert repr(phone) == "Phone('iPhone_apple', 100000, 20, 5)"
    assert str(phone) == 'iPhone_apple'
    assert phone.number_of_sim == 5


def test_add():
    """ Проверяем работу метода __add__"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
