import time
from threading import Thread


def long_time_task(i):
    time.sleep(2)
    return 8 ** 20


class MyThread(Thread):
    def __int__(self, target, args, name):
        Thread.__init__(self)
        self.target = target
        self.args = args
        self.name = name

    def run(self):
        print('子线程{}'.format(self.name))
        time.sleep(1)
        print('结束子线程{}'.format(self.name))


if __name__ == '__main__':
    start = time.time()
    l = []
    for i in range(4):
        t = MyThread(target=long_time_task, args=(i,), name=str(i))
        l.append(t)

    for t in l:
        t.start()
    for t in l:
        t.join()
    end = time.time()
    print('用时{}'.format(end - start))
