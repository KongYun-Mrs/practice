import threading
import time


class MyThread(threading.Thread):
    def __init__(self, target, args):
        self.target = target
        self.args = args
        threading.Thread.__init__(self)

    def run(self):
        add1(self.args)
        # time.sleep(1)
        print('Im {}'.format(self.name))


def add1(X):
    print('计算结果%d' % (X ** 2))


if __name__ == '__main__':
    l1 = []
    start_time = time.time()
    for i in range(4):
        t = MyThread(target=add1, args=i)
        l1.append(t)
    for i in l1:
        i.start()
    for i in l1:
        i.join()
    end_time = time.time()
    print('use time {}'.format(end_time - start_time))
