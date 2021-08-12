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


if __name__ == "__main__":
    moto = Moto()
    print(moto.oil)
    moto.oil = 100
    print(moto.oil)
    del moto.oil
    moto.oil
