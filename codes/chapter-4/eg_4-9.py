def say(greeting, describe, target):
    print(f'{greeting} {describe} {target}!')


if __name__ == "__main__":
    say('Hello', 'beautiful', 'Python')                       # 位置参数
    say(target='Python', greeting='Hello', describe='beautiful')  # 关键字参数
