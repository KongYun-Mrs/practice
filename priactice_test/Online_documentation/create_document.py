# -*- coding: utf-8 -*-
"""
Spyder Editor
this is just a test!
"""


class Test1():
    '''
    测试类，负责测试
    '''

    def hello(self):
        '''
        打印Hello
        :return:
        '''
        print("Python")

    def renren(self):
        '''
        测试Sphinx自动生成文档
        :return:
        '''
        print("自动生成文档")


class Test2():
    def test_2(self):
        '''
        hello
        :return:
        '''
        print("文档自动生成测试2")

    def renren_2(self):
        '''
        用Sphinx自动生成
        :return:
        '''
        print("自动生成文档2")


# -*-coding:utf-8-*-

def init_test():
    '''
    用于初始化项目测试，不需要任何参数
    :return:
    '''
    print("初始化项目")


def start():
    '''
    启动项目入口，
    :return:

    '''
    test(3)


def test(v):
    '''
    项目运行主要函数，需要传入一个参数n
    v:<int>
    :return:

    '''
    print(v)
