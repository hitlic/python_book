def say(greeting, describe, *, target):
    print(f'{greeting} {describe} {target}!')


if __name__ == "__main__":
    say('Hello', 'beautiful', target='Python')
    say('Hello',  'beautiful', 'Python')   # 没有使用关键字参数
