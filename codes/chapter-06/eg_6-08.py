class Name:
    def __init__(self, family_name, given_name):
        self.family_name = family_name
        self.given_name = given_name

    def __get__(self, obj, type):
        return f'{self.given_name} {self.family_name}'

    def __set__(self, obj, value):
        self.family_name = value[0]
        self.given_name = value[1]


class Person:
    name = Name('Rossum', 'Guido')


if __name__ == '__main__':
    p = Person()
    print(p.name)
    p.name = ('Gates', 'Bill')
    print(p.name)
