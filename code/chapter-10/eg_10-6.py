import os
import time
from multiprocessing import Process


class SubProcess(Process):
    def __init__(self, name_):
        self.__name = name_
        super().__init__()

    def run(self):
        print(f'这里是子进程{self.__name}')
        time.sleep(20)


if __name__ == '__main__':
    subp_A = SubProcess('A')
    subp_B = SubProcess('B')
    subp_A.start()
    subp_B.start()
    print(f'这里是父进程，进程ID为 {os.getpid()}')
    print(f'子进程A的ID为 {subp_A.pid}')
    print(f'子进程B的ID为 {subp_B.pid}')
    subp_A.join()
    subp_B.join()
