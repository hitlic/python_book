def create_averagers():
    numbers = []

    def avg1(num):
        numbers.append(num)
        return sum(numbers)/len(numbers)

    def avg2(num):
        numbers.append(num)
        return sum(numbers)/len(numbers)
    return avg1, avg2


if __name__ == "__main__":
    averager1, averager2 = create_averagers()
    print(averager1(3))
    print(averager2(5))
