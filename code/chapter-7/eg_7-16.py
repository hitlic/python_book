def division(x, y):
    '''
    除法运算
    Args:
        x: 数值1
        y: 数值2

    Example:
    >>> division(1, 1)
    1.0
    >>> division(1, 0)
    除数为0
    0
    >>> division(2, 1)
    2.0
    '''
    try:
        return x/y
    except ZeroDivisionError:
        print("除数为0")
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
