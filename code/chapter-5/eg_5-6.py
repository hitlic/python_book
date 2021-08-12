class TestHidden:
    def __init__(self):
        self.__hidden = 1

    def out(self):
        print(f'the hidden value is {self.__hidden}')

    def __hidden_value(self):
        return self.__hidden


if __name__ == "__main__":
    th = TestHidden()
    th.out()
    th.__hidden                     # 试图访问隐藏属性
    th.__hidden_value()             # 试图访问隐藏方法
