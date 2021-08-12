class Moto:
    def __init__(self):
        self.__oil = 0

    @property
    def oil(self):
        return self.__oil

    @oil.setter
    def oil(self, oil):
        self.__oil = oil

    @oil.deleter
    def oil(self):
        del self.__oil


class Wagon(Moto):
    @property
    def oil(self):
        return super().oil    # 调用基类对象中的oil


if __name__ == "__main__":
    wagon = Wagon()
    print(wagon.oil)
    wagon.oil = 1
