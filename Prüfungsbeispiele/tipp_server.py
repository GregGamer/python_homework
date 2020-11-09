import socket
from random import choice

serverSocket = socket.socket()                          # socket mit Defaulteinstellung erstellen
serverSocket.bind(('127.0.0.1', 1337))                  # Socket auf IP und Port binden
serverSocket.listen()                                   # Lauschen auf Portnr und IP
print('Waiting for Connection...')


clientSocket, clientAddressInfo = serverSocket.accept() # wartet auf Verbindung, wenn Verbindung da - dann clientSocket erstellt
# clientAddressInfo = (ip, port)        - Tuple
print(f'Verbundener Client: {clientAddressInfo}')       #clientAddressInfo[0] = IP, clientAddressInfo[1] = Portnr
money = 2
farben = ["blau", "rot", "gelb"]
msg = ""
while 1 < money <= 20:
    msg = clientSocket.recv(1024).decode('utf-8')           # b'hello\n\x214' deswegen .decode() -> hello
    if msg == "quit":
        break
    # "10 gelb
    money = int(msg.split(" ")[0])
    farbe = msg.split(" ")[1]
    gewinner_farbe = choice(farben)

    erg = [] # ["richtig"|"falsch", money*2]
    if gewinner_farbe == farbe :
        erg.append("richtig")
        erg.append(money*2)
        print(erg)
    else :
        erg.append("falsch")
        erg.append(0)
        print(erg)


    print(f'{clientAddressInfo}: {erg} , gewinner Farbe ist: {gewinner_farbe}')
    clientSocket.send(str(erg).encode('utf-8'))    # Nachricht an clientSocket senden

clientSocket.close()                                    # ClientSocket wird geschlossen
print(f'Client-Socket geschlossen')
serverSocket.close()                                    # ServerSocket wird geschlossen
print(f'Server-Socket geschlossen')
