# -*- coding: utf-8 -*-

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
        print u'create Iphone'


if __name__ == '__main__':
    phone_list = [u'xiaomi', u'iphone']
    for phone in phone_list:
        P = PhoneFactory(phone)
        P.create_phone()
