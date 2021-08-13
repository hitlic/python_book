class Test1:
    x = [0]


class Test2:
    def __init__(self):
        self.x = [0]


if __name__ == "__main__":
    t11 = Test1()
    t12 = Test1()
    t11.x[0] = 1
    print(t11.x, t12.x)

    t21 = Test2()
    t22 = Test2()
    t21.x[0] = 1
    print(t21.x, t22.x)
