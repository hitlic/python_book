def say(greeting, *describe, **detail):
    print(type(describe), type(detail))
    print(f'{greeting} {" and ".join(describe)} Python!')
    details = [f"It's {k} is {v}." for k, v in detail.items()]
    print(' '.join(details))


if __name__ == "__main__":
    say('Hello', 'beautiful', 'powerful', 'easy', syntax='elegant', code='simple')
