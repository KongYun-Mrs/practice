from socketserver import BaseRequestHandler, UDPServer
import time


class TimeHandler(BaseRequestHandler):
    def handler(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        print(resp)
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    print('11111111111')
    serv = UDPServer(('', 20000), TimeHandler)
    print(serv)
    serv.serve_forever()
