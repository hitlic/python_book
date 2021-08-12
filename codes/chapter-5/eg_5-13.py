import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        td = time.localtime()
        return cls(td.tm_year, td.tm_mon, td.tm_mday)


if __name__ == "__main__":
    today = Date.today()
    print(type(today))
    print(today.year)
