import socket, pickle

# HIER MUSS NICHTS GEMACHT WERDEN!!!

# Wird für das Empfangene Objekt benötigt
class Kontakt():
    def __str__(self):
        return f'{self.id}:\t{self.vname} {self.lname}\t{self.birthday}\t{self.age} Jahre \tVIP: {self.vip}\t aus {self.country}'

s = socket.socket()

s.bind(('127.0.0.1', 4444))
s.listen()

print('Waiting for Connection ...')
clientSocket, clientInfo = s.accept()
print('Client verbunden\n')

#Pickle liefert mir Objekt als String
for d in pickle.loads(clientSocket.recv(1024)):
    print(d)

print('\nwell done')