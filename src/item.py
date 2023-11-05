import csv
import os

class InstantiateCSVError(Exception):
    """
    Исключение при повреждении файла
    """

    def __init__(self):
        self.message = 'Файл items.csv поврежден'

    def __str__(self):
        return self.message


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
        super().__init__()

    @property
    def name(self):
        """добавлен геттер для name, используя @property"""

        return self.__name

    @name.setter
    def name(self, name_str):
        """добавлен сеттер для name, используя @property"""
        self.__name = name_str[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path='../src/items.csv'):
        """instantiate_from_csv() - класс-метод, инициализирующий
        экземпляры класса Item данными из файла src/items.csv"""

        try:
            # items_csv_read = os.path.join('../src/items.csv')
            # file_path = os.path.join(os.path.dirname(__file__), '..', file_path)
            with open(file_path, mode='r', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError
                cls.all.clear()
                for row in list(reader):
                    item = cls(row['name'], float(row['price']), int(row['quantity']))
                    if item not in cls.all:
                        cls.all.append(item)

        except InstantiateCSVError as error:
            print(error)
            return 'Файл items.csv поврежден'
            # raise InstantiateCSVError()
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
            return f"Отсутствует файл item.csv"

        #
        # except FileNotFoundError:
        #     print('Отсутствует файл items.csv')

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

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name



    # @staticmethod
    # def instantiate_from_csv_test(path):
    #     """
    #     Проверка наличия и целостности файла
    #     """
    #     try:
    #         file_path = os.path.join('../src/items.csv')
    #         with open(file_path, mode='r', encoding='windows-1251') as csvfile:
    #             reader = csv.DictReader(csvfile)
    #             for row in list(reader):
    #                 if (row.get('name') and row.get('price') and row.get('quantity')) in ['', None]:
    #                     raise InstantiateCSVError
    #                 if row['name'] != str or row['price'] != int or row['quantity'] != int:
    #                     print("Файл item.csv поврежден")
    #
    #     except FileNotFoundError:
    #         print('Отсутствует файл items.csv')
    #         return 'Отсутствует файл items.csv'
    #     except InstantiateCSVError as exep:
    #         print(exep.message)
    #         return exep.message








    # def instantiate_from_csv(self):
    #     try:
    #         open("items.csv")
    #     except FileNotFoundError:
    #         print("Отсутствует файл item.csv")
    #
    #     except InstantiateCSVError:
    #         print("InstantiateCSVError")
