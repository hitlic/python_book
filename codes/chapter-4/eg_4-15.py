def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    print(add(1, 1))
    print(add(1.0, 1.0))
    print(add.__annotations__)
