import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name  # атрибут name сделать приватным
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        """добавлен геттер для name, используя @property"""

        return self.__name

    @name.setter
    def name(self, name_str):
        """добавлен сеттер для name, используя @property"""
        self.__name = name_str[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path):
        """instantiate_from_csv() - класс-метод, инициализирующий
        экземпляры класса Item данными из файла src/items.csv"""

        # items_csv_read = os.path.join('../src/items.csv')
        file_path = os.path.join(os.path.dirname(__file__), '..', file_path)
        with open(file_path, mode='r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                if item not in cls.all:
                    cls.all.append(item)

    @staticmethod
    def string_to_number(num):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(num))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        return f"{self.__name}, {self.price}, {self.quantity}"
