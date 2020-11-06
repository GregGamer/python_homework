import socket

######CLIENT#######

clientSocket = socket.socket()                      # Socket mit Defaulteinstellung wird erstellt
clientSocket.connect(('127.0.0.1', 4444))           # Client versucht Verbindung zu IP und Port aufzubauen
print('Verbindung aufgebaut')


msg = input('Nachricht: ')                          # Userinput für Nachricht
clientSocket.send(msg.encode('utf-8'))              # msg wird an Server gesendet
recvMsg = clientSocket.recv(1024).decode('utf-8')   # empfangen einer Nachricht
print(recvMsg)

clientSocket.close()                                #ClientSocket geschlossen
print('Verbindung geschlossen')