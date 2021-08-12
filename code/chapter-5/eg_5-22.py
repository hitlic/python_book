class Moto:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def run(self, speed):
        print(f"本车为 Moto，长{self.width}，宽{self.length}，以速度{speed}行驶！")


class Wagon(Moto):
    def __init__(self, width, length, load):
        self.carrying_load = load            # 载客量
        Moto.__init__(self, width, length)


class Coach(Moto):
    def __init__(self, width, length, capacity):
        self.passenger_capacity = capacity   # 载重量
        Moto.__init__(self, width, length)


class Pickup(Wagon, Coach):
    def __init__(self, width, length, load, capacity):
        Wagon.__init__(self, width, length, load)
        Coach.__init__(self, width, length, capacity)

class Driver:
    def __init__(self, moto: Moto):
        self.moto = moto

    def drive(self, speed):
        self.moto.run(speed)


class Bouncy:
    def run(self, speed):
        print(f"这是一辆蹦蹦车，以速度{speed}行驶")


if __name__ == "__main__":
    pickup = Pickup(1.8, 3.9, 6, 20)
    bobo = Driver(pickup)
    bobo.drive(120)
    bouncy = Bouncy()
    bobo.moto = bouncy
    bobo.drive(2)
