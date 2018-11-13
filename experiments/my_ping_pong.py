import socketserver

host = "0.0.0.0"
port = 10000
address = (host, port)

class  TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        message = self.request.recv(10)
        print(f"got a message: {message}")

def serve():
    server = socketserver.TCPServer(address, TCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    serve()