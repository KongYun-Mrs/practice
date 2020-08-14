# coding: utf-8

import time
import json
import redis

from threading import Thread


class Consumer(Thread):
    def __init__(self):
        super(Consumer, self).__init__()
        self.queue = redis.Redis()

    def run(self):
        while True:
            try:
                num_tuple = self.queue.blpop('producer')
                a, b = json.loads(num_tuple[1].decode())
                print (a, b)
                sum = a + b
                print ('消费者消费了一组数{}'.format(sum))
                time.sleep(2)
            except Exception as e:
                print ('没有数据了')


consumer = Consumer()
consumer.start()
while True:
    time.sleep(1)
