def sort_key(e):
    return e[1]


if __name__ == "__main__":
    lst = [(1, 4), (2, 8), (5, 7)]
    print(sorted(lst, key=sort_key))
