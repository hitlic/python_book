def create_univariate_func(*prams):
    def univariate_func(x):
        y = 0
        order = len(prams) - 1
        for i, p in enumerate(prams):
            y += p * x**(order - i)
        return y
    return univariate_func


if __name__ == "__main__":
    uni_func = create_univariate_func(1, 2, 3)
    print(uni_func(1))
    print(uni_func(2))
    print(uni_func(3))
