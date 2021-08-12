# 直接方式
class Moto1:
    def __init__(self):
        self.oil = 0

# 间接方式
class Moto2:
    def __init__(self):
        self.__oil = 0
    
    def get_oil(self):
        return self.__oil
    
    def set_oil(self, oil):
        self.__oil = oil 

    