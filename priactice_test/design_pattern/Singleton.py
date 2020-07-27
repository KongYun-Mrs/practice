# 装饰器实现方式
def Singleton_test(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper


@Singleton_test
class A():
    X = 1

    def __init__(self, x):
        self.x = x


a1 = A(2)
a2 = A(3)
print(a1.x)
print(a2.x)


# __new__
class Singleton_B():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance


s1 = Singleton_B()
s2 = Singleton_B()
print(s1)
print(s2)
