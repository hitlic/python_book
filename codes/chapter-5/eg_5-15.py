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


if __name__ == "__main__":
    avg = Averager()
    avg.read([1, 2, 3])
    print(avg.value)
    avg.read({'a': 1, 'b': 2, 'c': 3})
    print(avg.value)
    avg.read('1, 2, 3')
    print(avg.value)
