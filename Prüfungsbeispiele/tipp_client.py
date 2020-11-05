import socket
import random
######CLIENT#######

ADDRESS = "127.0.0.1"
PORT = 1337

clientSocket = socket.socket()                      # Socket mit Defaulteinstellung wird erstellt
clientSocket.connect((ADDRESS, PORT))           # Client versucht Verbindung zu IP und Port aufzubauen
print(f'Connection to {ADDRESS}:{PORT} is established')

money = random.randint(5,15)

while money < 1 or money > 20 :
    print(f"Verfügbares Spielgeld: {money}€")
    msg = input('Dein Tipp <Einstatz> <blau|gelb|rot>: ') # "1 gelb"                      # Userinput für Nachricht
    msg_data = msg.split(" ")
    if len(msg_data) == 2 :
        if msg_data[0].isdigit() :
            tipp_money = int(msg_data[0])
            if tipp_money > money:
                print("Du hast nicht genug Geld!")
                continue 
        else :
            continue
        if msg_data[1] in ["blau", "rot", "gelb"]:
            tipp_farbe = msg_data[1]
        else :
            continue
        money = money - tipp_money
    else : 
        continue
    clientSocket.send(msg.encode('utf-8'))              # msg wird an Server gesendet

    recvMsg = clientSocket.recv(1024).decode('utf-8')   # empfangen einer Nachricht
    print(recvMsg)
    # ["richtig", 2]
    if recvMsg[0] == "richtig" :
        money = money + recvMsg[1]
    
    money = money + 2*tipp_money

clientSocket.close()                                #ClientSocket geschlossen
print('Verbindung geschlossen')