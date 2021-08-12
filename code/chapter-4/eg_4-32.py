from inspect import signature
from functools import wraps


def type_check(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        sig = signature(fun)                # 获取函数的签名
        param_dict = sig.parameters         # {参数: 类型}字典
        param_list = list(param_dict.values())
        for i, arg in enumerate(args):      # 检查位置参数
            assert type(arg) is param_list[i].annotation,\
                f'第{i+1}个参数的类型必须为{param_list[i].annotation}'
        for arg, value in kwargs.items():   # 检查关键字参数
            assert type(value) is param_dict[arg].annotation, \
                f'参数{arg}的类型必须为{param_dict[arg].annotation}'
        return fun(*args, **kwargs)
    return wrapper


@type_check
def fun(x: int, y: float):
    pass


if __name__ == "__main__":
    # fun(1, 2)
    # fun(1.0, 2)
    # fun(1, y=2)
    fun(1, 2.0)
