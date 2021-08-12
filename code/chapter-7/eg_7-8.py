def division(x, y):
    try:
        assert y != 1, '分母为1'
        return x/y
    except AssertionError as e:
        print(e)
        return x
    except Exception as e:
        print(e)
        return 0
