def say(greeting, /, describe, *, target):
    print(f'{greeting} {describe} {target}!')


if __name__ == "__main__":
    say('Hello', describe='beautiful', target='Python')
    say(greeting='Hello', describe='beautiful', target='Python')   # 没有使用位置参数
