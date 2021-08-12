
class Moto:
    def __init__(self):
        self.__oil = 0

    @property
    def oil(self):
        return self.__oil


if __name__ == "__main__":
    moto = Moto()
    print(moto.oil)
