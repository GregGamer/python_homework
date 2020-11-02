"""
Gregor Wagner
U6Bsp1.py - Echo Server - Server
Gregor Wagner, 52005240
"""
import socket

ADDRESS = "127.0.0.1"
PORT = 6666
RECV_BUFFER = 1024

serverSocket = socket.socket()

serverSocket.bind((ADDRESS, PORT))
serverSocket.listen()
print('Waiting for connection...')


clientSocket, clientAddressInfo = serverSocket.accept()
print(f'Verbunder Client: {clientAddressInfo}')

msg = ""
while msg != "quit" :
    msg = clientSocket.recv(RECV_BUFFER).decode("utf-8")
    clientSocket.send(msg.encode("utf-8"))
    print(f"{clientAddressInfo}: {msg}")

serverSocket.close()
print("Socket geschlossen")