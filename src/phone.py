from src.item import Item

class Phone(Item):

    """Phone содержит все атрибуты класса Item и
    дополнительно атрибут number_of_sim, содержащий количество поддерживаемых сим-карт"""

    def __init__(self, name, price, quantity, number_of_sim):
        self.number_of_sim = number_of_sim
        super().__init__(name, price, quantity)


    """Правильно ли, что оставила метод __add__ только в родительском клдассе Init???"""
    # def __add__(self, other):
    #     if not isinstance(other, Item):
    #         raise ValueError('Складывать можно только объекты Item и дочерние от них.')
    #     return self.quantity + other.quantity

    def __repr__(self):
        """Изменила логику __repr__, добавив инициализированный number_of_sim"""
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
