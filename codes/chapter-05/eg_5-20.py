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
    @Moto.oil.getter
    def oil(self):
        return super.oil

    @Moto.oil.setter
    def oil(self, oil):
        super(Wagon, Wagon).oil.__set__(self, oil)


if __name__ == "__main__":
    wagon = Wagon()
    wagon.oil = 100
    print(wagon.oil)
