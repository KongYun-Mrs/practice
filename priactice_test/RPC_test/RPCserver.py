# -*- coding:UTF-8 -*-
# ! /usr/bin/env python
import json
import socket
import time
import struct


def handle_conn(conn, addr, handlers):
    print(addr, handlers)
    while True:
        length_prefix = conn.recv(4)  # 请求长度前缀
        if not length_prefix:
            print('Bye')
            conn.clsoe()
            break
        length, = struct.unpack('l', length_prefix)
        body = conn.recv(length)  # 接收客户端数据
        request = json.loads(body)
        in_ = request['in']
        params = request['params']
        handler = handlers[in_]  # 查找请求处理器
        handler(conn, params)  # 处理请求


def loop(sock, handlers):
    while True:
        conn, addr = sock.accept()  # 接收连接
        handle_conn(conn, addr, handlers)  # 处理连接


def send_result(conn, out, result):
    response = json.dumps({'out': out, 'result': result})
    length_prefix = struct.pack('l', len(result))  # 响应前缀
    conn.sendall(length_prefix)
    conn.sendall(response.encode('utf-8'))


def ping(conn, params):
    send_result(conn, 'pong', params)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 8080))  # 绑定端口
    sock.listen(1)
    headers = {'ping': ping}
    loop(sock, headers)
