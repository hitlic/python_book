def fun(param):
    assert isinstance(param, str), '参数必须为字符串'


if __name__ == '__main__':
    fun('abc')
    fun(1)
