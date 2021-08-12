class ParameterException(Exception):
    pass


def greeting(info):
    if not isinstance(info, str):
        raise ParameterException("参数必须为字符串！")
    print(info)


if __name__ == '__main__':
    greeting("Hello Python")
    greeting(1)
