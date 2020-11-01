"""
Gregor Wagner
U6Bsp1.py - Echo Server - Client
Gregor Wagner, 52005240
"""
import socket

ADDRESS = "127.0.0.1"
PORT = 1337
RECV_BUFFER = 1024

clientSocket = socket.socket()


try:
    print("Establishe Connection...")
    clientSocket.connect((ADDRESS, PORT))
    print(f"Connection to {ADDRESS}:{PORT} is established")
except ConnectionRefusedError as e:
    print(e)
    quit()



msg = ""
while msg.lower() != "quit" :
    msg = input("> ")
    clientSocket.send(msg.encode("utf-8"))
    print("Server Echo: "+clientSocket.recv(RECV_BUFFER).decode("utf-8").upper()+"\n")

clientSocket.close()
