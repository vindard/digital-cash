import socketserver

host = "0.0.0.0"
port = 10000
address = (host, port)

class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class  TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        message = self.request.recv(10).strip()
        print(f"got a message: {message}")

        if message == b'ping':
            self.request.sendall(b"pong\n")

def serve():
    server = MyTCPServer(address, TCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    serve()