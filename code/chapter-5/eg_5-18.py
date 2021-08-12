class Moto:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def run(self, speed):
        print(f"本车为 Moto，长{self.width}，宽{self.length}，\
                以速度{speed}行驶！")


class Wagon(Moto):
    def __init__(self, width, length, load):
        self.carrying_load = load            # 载客量
        Moto.__init__(self, width, length)


class Coach(Moto):
    def __init__(self, width, length, capacity):
        self.passenger_capacity = capacity   # 载重量
        Moto.__init__(self, width, length)
