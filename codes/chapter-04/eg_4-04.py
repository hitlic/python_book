def copy(seq):
    return [copy(o) if type(o) is list else o for o in seq]


if __name__ == "__main__":
    lst = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10, 11]]]]]
    lst_new = copy(lst)
    lst_new[2][2][2][2][2] = 0
    print(lst)
    print(lst_new)
