class Moto:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def run(self, speed):
        print(f"本车为 Moto，长{self.width}，宽{self.length}，\
                以速度{speed}行驶！")


class Wagon(Moto):
    def run(self, speed):
        print(f"本车为 Wagon，长{self.width}，宽{self.length}，以速度{speed}行驶！")


if __name__ == "__main__":
    wagon = Wagon(2.2, 10)
    wagon.run(50)
