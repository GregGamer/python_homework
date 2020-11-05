import socket

serverSocket = socket.socket()                          # socket mit Defaulteinstellung erstellen
serverSocket.bind(('127.0.0.1', 1337))                  # Socket auf IP und Port binden
serverSocket.listen()                                   # Lauschen auf Portnr und IP
print('Waiting for Connection...')


clientSocket, clientAddressInfo = serverSocket.accept() # wartet auf Verbindung, wenn Verbindung da - dann clientSocket erstellt
# clientAddressInfo = (ip, port)        - Tuple
print(f'Verbundener Client: {clientAddressInfo}')       #clientAddressInfo[0] = IP, clientAddressInfo[1] = Portnr

msg = clientSocket.recv(1024).decode('utf-8')           # b'hello\n\x214' deswegen .decode() -> hello
print(f'{clientAddressInfo}: {msg}')
clientSocket.send(f'{msg.upper()} - Nachricht erhalten'.encode('utf-8'))    # Nachricht an clientSocket senden

clientSocket.close()                                    # ClientSocket wird geschlossen
print(f'Client-Socket geschlossen')
serverSocket.close()                                    # ServerSocket wird geschlossen
print(f'Server-Socket geschlossen')
