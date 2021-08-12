def test_dict():
    pass


if __name__ == '__main__':
    print(test_dict.__dict__)
    test_dict.x = 0
    print(test_dict.__dict__)
