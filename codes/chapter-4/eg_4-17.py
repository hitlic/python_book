def outer():
    def inner():
        print("This is from inner")
    print("This is from outer")
    inner()

if __name__ == "__main__":
    outer()
    