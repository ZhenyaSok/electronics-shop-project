class Item:
    """Заявленная скидка"""
    pay_rate = 0.85
    all = []

    def __init__(self, name_product, price, quantity_product):
        self.name_product = name_product
        self.price = price
        self.quantity_product = quantity_product

        Item.all.append(self)

    def apply_discount(self):
        """Метод для применения скидки."""
        self.price *= self.pay_rate

    def calculate_total_price(self):
        """Метод высчитывает общую цену за всё количество товара"""
        return self.price * self.quantity_product

    def __repr__(self):
        return f"{self.name_product}, {self.price}, {self.quantity_product}"



"""Экземпляр класса Item содержит атрибуты:

название товара
цена за единицу товара
количество товара в магазине
Класс Item поддерживает два атрибута класса:

для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
для хранения созданных экземпляров класса
Реализуйте методы, позволяющие:

получить общую стоимость конкретного товара в магазине
применить установленную скидку для конкретного товара
Тестирование:

Напишите тесты в tests/test_item.py"""
