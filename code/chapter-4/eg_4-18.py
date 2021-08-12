def create_averager():
    numbers = []

    def avg(nums):
        if isinstance(nums, list):
            numbers.extend(nums)
        else:
            numbers.append(nums)
        return sum(numbers)/len(numbers)
    return avg


if __name__ == "__main__":
    averager = create_averager()
    print(averager([3, 5]))
    print(averager(7))
    print(averager([8, 9]))
