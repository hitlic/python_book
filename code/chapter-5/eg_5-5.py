class TestDel:
    def __del__(self):
        print(f'{self}对象被销毁')


if __name__ == "__main__":
    td = TestDel()
    del td     # 删除对象
