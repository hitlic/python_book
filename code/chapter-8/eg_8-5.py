class File:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print("进入上下文环境...")
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("离开上下文环境...")
        self.file.close()
        print('异常类型：', exc_type)
        print('异常值：', exc_val)
        print('异常跟踪：', exc_tb)
        return True               # 不再抛出with语句块中的异常
        # return False            # 抛出with语句块中的异常


if __name__ == '__main__':
    with File('test_file', 'w') as f:
        f.write('file contents')
        raise Exception('程序运行发生异常')
