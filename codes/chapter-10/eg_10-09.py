def test_coroutine():
    while True:
        x = yield
        print(f"传入的值为{x}")


if __name__ == '__main__':
    tc1 = test_coroutine()
    tc2 = test_coroutine()
    next(tc1)    # 预激活协程tc1
    next(tc2)    # 预激活协程tc2
    tc1.send(0)
    tc2.send(1)
    tc1.close()
    tc2.close()
    tc1.send(0)
