class Moto:                       # 具体类
    def __init__(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity


class CoachMixIn:                 # 混入类
    def carry_passengers(self, nums):
        capacity = super().get_capacity()
        if nums > capacity:
            print("人员超载！")
        else:
            print(f"搭载{nums}名乘客！")


class Car(CoachMixIn, Moto):      # 被混入类
    def __init__(self, capacity):
        super().__init__(capacity)
        self.capacity = capacity


if __name__ == "__main__":
    car = Car(5)
    car.carry_passengers(10)
    car.carry_passengers(3)
