# -*- coding: utf-8 -*-
from multiprocessing import Process
import signal
import sys

import eventlet
import socketio

clients = {}


def run(port):
    sio = socketio.Server()
    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'index.html'}
    })

    @sio.event
    def connect(sid, environ):
        print('connect ', sid)

    @sio.event
    def disconnect(sid):
        print('disconnect ', clients[sid])

    print('启动服务器', port)
    eventlet.wsgi.server(eventlet.listen(('', port)), app)


if __name__ == '__main__':
    p = Process(target=run, args=(9090,))
    p.daemon = True
    p.start()
    # p.terminate()
    print('主进程启动')


    def signal_handler(signal, frame):
        print('关闭从进程')
        # p.terminate()
        print('主进程退出')
        sys.exit(0)


    signal.signal(signal.SIGINT, signal_handler)
    while True:
        pass
