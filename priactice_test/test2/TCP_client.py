from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('localhost', 500))
s.send(b'Hello')
s.recv(8192)