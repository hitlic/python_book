class Fibonacci:
    def __init__(self, max=100):
        self.v1 = 0
        self.v2 = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        value = self.v2
        if value >= self.max:
            raise StopIteration
        self.v1, self.v2 = self.v2, self.v1 + self.v2
        return value


if __name__ == '__main__':
    fb = Fibonacci()
    print(iter(fb))
    print(next(fb))
    fb = Fibonacci()
    print(list(fb))
