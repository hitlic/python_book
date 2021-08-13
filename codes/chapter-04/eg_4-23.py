def run_chance(fun):
    print(f'装饰函数 {fun.__name__}')
    return fun


@run_chance
def fun1():
    print('运行函数fun1')


@run_chance
def fun2():
    print('运行函数fun2')


if __name__ == '__main__':
    fun1()
    fun2()
