def say(greeting='Hello', *describe):
    print(type(describe))
    print(f'{greeting} {" and ".join(describe)} Python!')


if __name__ == "__main__":
    say('Hello', 'beautiful', 'powerful', 'easy')
