class Moto:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def run(self, speed):
        print(f"本车为 Moto，长{self.width}，宽{self.length}，\
                以速度{speed}行驶！")


class Wagon(Moto):
    pass


class Coach(Moto):
    pass


class Car(Coach):
    pass


class Bus(Coach):
    pass
