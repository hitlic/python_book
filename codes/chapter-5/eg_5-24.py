class Moto:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        print('执行Moto类 __init__ 方法')


class Wagon(Moto):
    def __init__(self, width, length):
        super().__init__(width, length)
        print('执行Wagon类 __init__ 方法')


class Coach(Moto):
    def __init__(self, width, length):
        super().__init__(width, length)
        print('执行Coach类 __init__ 方法')


class Pickup(Wagon, Coach):
    def __init__(self, width, length):
        super(Pickup, self).__init__(width, length)
        print('执行Pickup类 __init__ 方法')


if __name__ == "__main__":
    pickup = Pickup(1.8, 3.9)
