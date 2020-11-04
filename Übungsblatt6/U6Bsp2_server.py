"""
Gregor Wagner
U6Bsp2.py - Chat Programm - server
Gregor Wagner, 52005240
"""
import sys, socket

ADDRESS = "127.0.0.1"
PORT = 1337
BUFFER_SIZE = 1024

class Server() :
    def __init__(self, host, port) :
        self.host = host
        self.port = port

    def bind(self) :
        self.socket = socket.socket((self.host, self.port))
        self.socket.listen()
        self.conn, self.addr = self.socket.accept()

    def send(self, msg) :
        self.socket.sendall(msg)

    def receive(self) :
        return self.socket.recv(BUFFER_SIZE)

    def broadcast(self, msg) :
        self.conn.sendall(msg)

    def stop(self) :
        pass

