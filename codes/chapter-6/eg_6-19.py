import time

class RunTime():
    def __init__(self, fun):
        self.fun = fun

    def __call__(self):
        start = time.time()
        result = self.fun()
        end = time.time()
        print(f'函数{self.fun.__name__}的执行时间为{(end-start):.4}秒')
        return result

@RunTime
def test_fun():
    time.sleep(1)
if __name__ == '__main__':
    print(test_fun)
    test_fun()
        
