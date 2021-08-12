from collections import abc


class MSeqAbc(abc.MutableSequence):
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        self._values[index] = value

    def __delitem__(self, index):
        del self._values[index]

    def insert(self, index, value):
        self._values.insert(index, value)


class MSeqDuck:
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        self._values[index] = value

    def __delitem__(self, index):
        del self._values[index]

    def insert(self, index, value):
        self._values.insert(index, value)


if __name__ == '__main__':
    msabc = MSeqAbc([1, 2, 3])
    print(len(msabc))
