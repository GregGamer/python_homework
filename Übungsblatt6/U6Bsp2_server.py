"""
Gregor Wagner
U6Bsp2.py - Chat Programm - server
Gregor Wagner, 52005240
"""
import sys, socket, threading

ADDRESS = "127.0.0.1"
PORT = 1337
BUFFER_SIZE = 1024

class Server() :
    def __init__(self, host, port) :
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.clientConnections = []

    def bind(self) :
        self.clientConnections.append(self.socket.accept())

    def send(self, msg) :
        self.clientConnections[0][0].send(msg.encode("utf-8"))

    def receive(self) :
        return self.clientConnections[0][0].recv(BUFFER_SIZE).decode("utf-8")

    def broadcast(self, msg) :
        # self.conn.sendall(msg)
        pass

    def stop(self) :
        self.socket.close()


def main() :
    server = Server(ADDRESS, PORT)
    server.bind()
    recvMsg = ""
    while recvMsg != "quit" :
        recvMsg = server.receive()
        print(recvMsg)
        server.send(recvMsg)

    server.stop()



if __name__ == "__main__":
    main()


