# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

index = u'test_audit'
ES = Elasticsearch(hosts=u'127.0.0.1:9200', timeout=30, max_retries=10, retry_on_timeout=True)


# 创建索引
def create_index():
    result = ES.indices.create(index=index)
    return result


# 插入数据
def add_shuju():
    # data = {'id': 1, 'name': 'kongyun', 'age': 25}
    data = {'id': 2, 'name': 'zhangsan', 'age': 24}
    result = ES.index(index=index, doc_type=index, body=data, request_timeout=30)
    print 'Success!'


def search():
    S = Search(using=ES, index=index)
    if ES.indices.exists("test_audit") is not True:
        ES.indices.create(index="test_audit")
    res = S.query('match', name='zhangsan').sort("_id").execute()
    return res


if __name__ == '__main__':
    # 添加数据
    add_shuju()
    # 数据查询
    res = search()
    print res.hits.hits
