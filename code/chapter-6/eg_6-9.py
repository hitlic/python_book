from functools import singledispatchmethod


class Averager:
    @singledispatchmethod
    def read(self, data):
        n = len(data)
        self.value = sum(data)/n

    @read.register(dict)
    def _(self, data):
        data = data.values()
        n = len(data)
        self.value = sum(data)/n

    @read.register(str)
    def _(self, data):
        data = [float(i) for i in data.split(',')]
        n = len(data)
        self.value = sum(data)/n

    def __call__(self, data):
        self.read(data)
        return self.value


if __name__ == '__main__':
    avg = Averager()
    print(avg([1, 2, 3, 4]))
    print(avg('1, 2, 3, 4'))
