import time


class CodeRunTime:
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'代码块运行时间：{time.perf_counter() - self.start}')
        return False


if __name__ == '__main__':
    with CodeRunTime():
        lst = []
        for i in range(1000000):
            lst.append(i)
