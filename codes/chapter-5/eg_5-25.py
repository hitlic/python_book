class Moto:                       # 具体类
    def run(self, speed):
        print(f"本车为{self.__class__.__name__}，以速度{speed}行驶！")


class WagonMixIn:                 # 混入类
    def carry_cargo(self):
        print("装载货物！")


class CoachMixIn:                 # 混入类
    def carry_passengers(self):
        print("搭载乘客！")


class Truck(WagonMixIn, Moto):    # 被混入类
    pass


class Car(CoachMixIn, Moto):      # 被混入类
    pass


if __name__ == "__main__":
    car = Car()
    car.run(80)
    car.carry_passengers()
    truck = Truck()
    truck.run(60)
    truck.carry_cargo()
