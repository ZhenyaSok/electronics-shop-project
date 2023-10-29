from src.item import Item


class MixinLog:
    __language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):

        if self.language.upper() == 'RU':
            self.__language = 'EN'
        else:
            self.__language = "RU"
            # else:
            #     self.__language = "EN"
        return self


class Keyboard(Item, MixinLog):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
