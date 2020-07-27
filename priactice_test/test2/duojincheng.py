from multiprocessing import Pool, cpu_count
import os
import time


def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__ == '__main__':
    print('当前母进程{}'.format(os.getpid()))
    start = time.time()
    p = Pool(4)
    # 开启子进程
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有进程结束')
    p.close()
    p.join()
    end = time.time()
    print('用时{}'.format(end - start))
