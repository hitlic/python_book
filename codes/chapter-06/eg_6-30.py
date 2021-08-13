class Field:                                  # 数据库列的基类
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f'{self.__class__.__name__}:{self.name}'


class StrField(Field):                        # 字符类型的列
    def __init__(self, name):
        super().__init__(name, 'varchar(50)')


class IntField(Field):                        # 整数类型的列
    def __init__(self, name):
        super().__init__(name, 'int')


class ModelMetaclass(type):                   # 数据库表的元类
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings:
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):  # 数据库表的基类
    def __getattr__(self, key):
        return self.get(key, None)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = f'insert into {self.__table__} ({",".join(fields)}) values ({",".join(params)})'
        print(sql, tuple(args))


class User(Model):
    # 定义类的属性到数据库列的映射：
    id = IntField('id')
    name = StrField('username')
    password = StrField('password')


if __name__ == '__main__':
    u1 = User(id=1, name='张三', password='123456')
    u1.save()
    u2 = User(id=2, name='李四', password='123456')
    u2.save()
