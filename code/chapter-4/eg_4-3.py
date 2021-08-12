def fun1(formal_p):
    formal_p = [8, 5, 7]


def fun2(formal_p):
    formal_p[0] = 0


if __name__ == "__main__":
    actual_p = [1, 4, 2]
    fun1(actual_p)
    print(actual_p)      # 实参不变
    fun2(actual_p)
    print(actual_p)      # 实参发生了变化
