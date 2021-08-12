def cumulative_average():
    n = 0
    total = 0
    avg = 0
    while True:
        x = yield avg
        total += x
        n += 1
        avg = total/n


if __name__ == '__main__':
    ca = cumulative_average()
    print(next(ca))
    print(ca.send(5))
    print(ca.send(15))
    print(ca.send(10))
    ca.close()
