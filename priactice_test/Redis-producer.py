# coding: utf-8

import time
import redis
import json
import random

from threading import Thread


class Producer(Thread):
    def __init__(self):
        super(Producer, self).__init__()
        self.queue = redis.Redis()

    def run(self):
        while True:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
            print ('生产者生产了两个数字{},{}'.format(a, b))
            self.queue.rpush('producer', json.dumps((a, b)))
            time.sleep(2)


if __name__ == '__main__':
    producer = Producer()
    producer.start()
    while True:
        time.sleep(1)
