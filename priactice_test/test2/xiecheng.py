# -*- coding: utf-8 -*-
# socket网络编程
# 协程异步 非阻塞  会自动判断yu
import Queue

import gevent
from gevent import monkey, socket

socket_server = socket.socket()
socket_server.bind(('0.0.0.0', 8080))
socket_server.listen(1000)
q = Queue.Queue(3)


def conmuer(connect):
    while True:
        massage = connect.recv(1024)
        if massage:
            print(massage)
            gevent.sleep(1)
            connect.send(massage)
        else:
            connect.close()
            break


def conmuer1(connect):
    while True:
        # massage = connect.recv(1024)
        massage = u'Unhappy!'
        if massage:
            print(massage + '!!!!')
            gevent.sleep(1)
        else:
            connect.close()
            break


while True:
    connect, address = socket_server.accept()
    g1 = gevent.spawn(conmuer, connect)  # 创建协程
    g2 = gevent.spawn(conmuer1, connect)  # 创建协程
    gevent.joinall([g1, g2])  # 执行所有协程
