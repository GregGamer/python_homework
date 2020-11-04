"""
Gregor Wagner
U6Bsp2.py - Chat Programm - client
Gregor Wagner, 52005240
"""
import sys, socket

ADDRESS = "127.0.0.1"
PORT = 1337
BUFFER_SIZE = 1024

class Client() :
    def __init__(self, host, port, nickname) :
        self.host = host
        self.port = port
        self.nickname = nickname

    def bind(self) :
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    def send(self, msg) :
        self.socket.send(msg.encode("utf-8"))

    def receive(self) :
        return self.socket.recv(1024).decode("utf-8")

    def stop(self) :
        self.socket.close()



def main():
    if len(sys.argv) > 1 :
        nickname = sys.argv[1]
    else :
        nickname = "unknown"

    client = Client(ADDRESS, PORT, nickname)

    client.bind()
    while (msg := input("> ")) != "quit" :
        client.send(msg)
        print(client.receive())

    client.stop()



if __name__ == "__main__":
    main()

