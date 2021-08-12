def fun():
    def inner_fun():
        print('This is inner fun!')
    print('This is fun!')
    inner_fun()


if __name__ == "__main__":
    fun()
