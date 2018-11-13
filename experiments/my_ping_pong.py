import SocketServer

host = "0.0.0.0"
port = 10000
address = (host, port)

class  TCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        message = self.request.recv(10)
        print(f"got a message: {message}")

def serve():
    server = SocketServer.TCPServer(address, TCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    serve()