from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    print('1111111111111')
    def handle(self):
        print('GOT connection from ', self.client_address)
        while True:
            msg = self.request.recv(8192)  # 设置缓存
            print(msg)
            if not msg:
                break
            self.request.send(msg)



server = TCPServer(('', 500), EchoHandler)
server.serve_forever()
