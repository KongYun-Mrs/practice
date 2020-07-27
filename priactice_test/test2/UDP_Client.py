from socket import socket, AF_INET, SOCK_DGRAM


s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('127.0.0.1', 20000))
s.recvfrom(8192)
