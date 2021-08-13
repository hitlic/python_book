import os
import time
from multiprocessing import Process


def target_fun(name_):
    print(f'这里是子进程{name_}')
    time.sleep(20)


if __name__ == '__main__':
    subp_A = Process(target=target_fun, args='A')
    subp_B = Process(target=target_fun, args='B')
    subp_A.start()
    subp_B.start()
    print(f'这里是父进程，进程ID为 {os.getpid()}')
    print(f'子进程A的ID为 {subp_A.pid}')
    print(f'子进程B的ID为 {subp_B.pid}')
    subp_A.join()
    subp_B.join()
