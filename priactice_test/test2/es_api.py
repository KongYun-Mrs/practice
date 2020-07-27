# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

index = u'new_weather'
ES = Elasticsearch(hosts=u'127.0.0.1:9200', timeout=30, max_retries=10, retry_on_timeout=True)


# 创建索引
def create_index():
    result = ES.indices.create(index=index)
    return result


# 插入数据
def add_shuju():
    data = {'id': 2, 'name': 'zhangsan', 'last_time_used': "2020-07-09 17:31:12"}
    try:
        result = ES.index(index=index, doc_type='politics', body=data)
        print 'Success!'
        print result
    except Exception as e:
        print e


def search():
    S = Search(using=ES, index=index)
    if ES.indices.exists("new_weather") is not True:
        ES.indices.create(index="new_weather")
    res = S.query('match', name='wangwu').sort("_id").execute()
    print (res.hits.hits)
    for data in res.hits.hits:
        print data
    return res


if __name__ == '__main__':
    # 添加数据
    # add_shuju()
    search()
