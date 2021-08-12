# 文件 test_profile.py
def fabnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabnacci(n - 1) + fabnacci(n - 2)


def fabnacci_list(n):
    lst = []
    if n > 0:
        lst.extend(fabnacci_list(n - 1))
    lst.append(fabnacci(n))
    return lst


if __name__ == '__main__':
    fabnacci_list(30)
