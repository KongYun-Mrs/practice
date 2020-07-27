# -*- coding: utf-8 -*-
from gevent import monkey, socket

if __name__ == '__main__':
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.connect(('127.0.0.1', 8080))
    while True:
        msg = 'hello1'
        try:
            socket_server.sendall(msg)
        except Exception as e:
            print (e)
