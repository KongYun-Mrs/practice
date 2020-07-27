from multiprocessing import Pool
import time
from multiprocessing import Process


def func(n):
    n += 1


if __name__ == '__main__':
    start_time = time.time()
    P = Pool(processes=4)
    map(func, range(1000))
    end_time = time.time()
    print(end_time - start_time)

    l = []
    for i in range(1000):
        p = Process(target=func, args=(i,))
        p.start()
        l.append(p)
        print(p.pid)
        [i.join() for i in l]
