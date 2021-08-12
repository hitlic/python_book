def division(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("除数为0")
    return 0


if __name__ == '__main__':
    division(1, 2)
    division(1, 0)
