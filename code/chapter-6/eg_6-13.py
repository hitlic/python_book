class GenIter:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        for v in self.values:
            yield v
        # yield from self.values  # 与前两行循环语句等价


if __name__ == '__main__':
    gi = GenIter([1, 2, 3])
    print(iter(gi))
    for n in gi:
        print(n)
