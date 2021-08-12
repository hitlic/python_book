def division(x, y):
    try:
        assert y != 1, '分母为1'
        return x/y
    except (AssertionError, Exception) as e:
        print(e)