class Auto:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def run(self, speed):
        print(f"本车长{self.width}，宽{self.length}，以速度{speed}行驶！")


if __name__ == "__main__":
    auto = Auto(1.5, 3.3)
    auto.run(80)
