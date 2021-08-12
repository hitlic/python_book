def division(x, y):
    try:
        assert y != 1, '分母为1'
        return x/y
    except Exception as e:
        print(e)


if __name__ == '__main__':
    division(1, 1)
    division(1, 0)
