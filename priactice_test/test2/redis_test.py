# -*- coding: utf-8 -*-

# str = '\u5185\u90e8\u6267\u884c\u9519\u8bef'
# print str.encode('utf-8').decode('unicode_escape')
# s1 = {17}
# s2 = {14, 15, 16}
# print s1.difference(s2)
import json

import redis

redis_conifg = {'host': 'localhost', 'port': 6379, 'db': 0}


def redis_connecnt():
    try:
        R = redis.Redis(**redis_conifg)
        return R
    except Exception as e:
        print e


def add_detail():
    r = redis_connecnt()
    data = {'user': 'zhangsan', 'age': 12}
    list1 = [1, 2, 23, 40]
    value = json.dumps(data)
    r.set(name='test', value=value, ex=20)
    r.rpush('test_list', *list1)
    print u'添加成功'


def search():
    r = redis_connecnt()
    list1 = []
    while True:
        index = r.lpop('test_list')
        list1.append(index)
        if index is None:
            return list1


if __name__ == '__main__':
    add_detail()
    index = search()
    print index
