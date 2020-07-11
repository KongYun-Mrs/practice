from threading import Thread


def test(args):
    print "{}".format(args)


if __name__ == '__main__':
    for i in range(4):
        t1 = Thread(test(i))
        t1.start()
