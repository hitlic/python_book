while True:
    try:
        value = input("请输入一个数字：")
        value = float(value)
    except Exception as e:
        print("输入错语，请再次尝试！")
    else:
        print("输入正确！")
        break
