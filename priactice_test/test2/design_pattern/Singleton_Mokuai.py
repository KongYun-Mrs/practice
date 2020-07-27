# coding: utf-8

class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()

# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
