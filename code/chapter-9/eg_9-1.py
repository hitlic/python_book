import time


def fun():
    sum_value = 0
    for i in range(1000000):
        sum_value += i


# 使用perf_counter函数
start = time.perf_counter()
fun()
time.sleep(1)
end = time.perf_counter()
print('perf_counter:', end - start)

# 使用process_time函数
start = time.process_time()
fun()
time.sleep(1)
end = time.process_time()
print('process_time:', end - start)
