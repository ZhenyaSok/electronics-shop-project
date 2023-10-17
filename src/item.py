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
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        self.__name = name_str[:10]


    @classmethod
    def instantiate_from_csv(cls):
        """instantiate_from_csv() - класс-метод, инициализирующий
        экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        items_csv_read = os.path.join('../src/items.csv')
        with open(items_csv_read, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = []
            for row in reader:
                item = cls(row['name'], row['price'], row['quantity'])
                cls.all.append(item)
                # name = row['name']
                # price = float(row['price'])
                # quantity = int(row['quantity'])
                # item = cls(name, price, quantity)
                # items.append(item)



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


    # def __repr__(self):
    #     return f"{self.__name}, {self.price}, {self.quantity}"
