class MyList:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = list(values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __len__(self):
        return len(self.values)

    def __delitem__(self, key):
        del self.values[key]

    def __reversed__(self):
        return reversed(self.values)

    def add(self, value):
        self.values.append(value)

    def __str__(self):
        return str(self.values)


if __name__ == '__main__':
    ml = MyList()
    print(ml)
    ml.add(0)
    ml.add(1)
    del ml[1]
    print(len(ml))
    print(ml)
    print(0 in ml)
