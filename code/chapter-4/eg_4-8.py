x = 0
def fun():
    global x
    x = 1
    print(x)


if __name__ == "__main__":
    fun()
    print(x)