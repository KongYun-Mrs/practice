# -*- coding: utf-8 -*-
# list1 = ['1', '2', '3']
# list = []
# # for i in list1:
# a = ','.join(list1)
# print a
# list.append(['1', 'b', a])
# print list
#
#
# l1 = [1, 2, 3]
# s = str(l1).strip('[]')
# print s, type(s)
#
# # ls=['\xd4','\xb6', '\xb3', '\xcc', '\xbf', '\xd8', '\xd6', '\xc6']
# # ch=''.join(ls)
# # ss=ch.decode('gbk')
# # print (ss.encode('utf-8'))
#
#
# s2 = "u'\u6076\u610f\u7a0b\u5e8f\u5165\u4fb5'"
# print s2
# import time
#
# s1 = 1581492062495
# s2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(s1) / 1000))
# print s2


# s1 = u'哈咯'
# print type(s1)
# print(type(s1.encode('utf-8')))
# print type(s1)

# s2 = u'asdasd'
# print type(s2)
# print type(s2.encode('utf-8'))


# s1 = u'归并告警导出2020-01-11 00-00-00至2020-04-09 23-59-59.xlsx'
# print s1.encode('utf-8')
# import time
#
# time1 = time.time()
# print time1
# print type(time1)

# lis1 = [11,22,33,44]
# print max(lis1)

# a = 1
# if a:
#     x = 3
# x = 4
# print x


# with open('./souye.txt', 'a+') as fp:
#     fp.write(chart_cls + '\n')


# def html_special(in_str):
#     try:
#         dd = {"<": "&lt;", ">": "&gt;", "'": "&#039;", '"': '&quot;', "&": "&#039;"}
#         for i in dd:
#             in_str = in_str.replace(i, dd[i])
#     except:
#         pass
#     return in_str
#
#
# name = '<img src=1 onerror=alert(7777);>'
# name1 = html_special(name)
# print name1
# item1 = ["防火墙", "杀毒"]
# # print (str(item1).strip('[').strip(']')).decode('unicode_escape')
# print ",".join(item1)


# 工厂模式
class PhoneFactory():
    def __init__(self, phonetype):
        self.phonetype = phonetype

    def create_phone(self):
        if self.phonetype == u'xiaomi':
            xiaomi = xiaomi_phone()
            xiaomi()
        if self.phonetype == u'iphone':
            IP = iphone()
            IP()


class xiaomi_phone():
    def __call__(self, *args, **kwargs):
        print u'create xiaomi'


class iphone():
    def __call__(self, *args, **kwargs):
        print u'create xiaomi'


if __name__ == '__main__':
    phone_list = [u'xiaomi', u'iphone']
    for phone in phone_list:
        P = PhoneFactory(phone)
        P.create_phone()

# def is_special_character(c):
#     sets = [42, 34, 39, 60, 62, 37]  # *" '<>%
#     # sets = range(33, 48)  # ! " # $ % & ' ( ) * + , - . /
#     # sets.extend(range(58, 65))  # : ; < = > ? @
#     return ord(c) in sets


# print is_special_character("<script>")


A = divmod(5, 10)
print A
