import pickle       # wird für s.send verwendet

class Kontakt():


    def __init__(self, id, vname, lname, birthday, country, vip):
        #ToDo  -> Werte zuweisen; vorher normalisieren (alles groß/klein schreiben, etc.)
        self.id = None
        self.vname = None
        self.lname = None
        self.birthday = None
        self.country = None
        self.vip = None
        self.age = self.calcAge()

    # Alter berechnen und zurückgeben; wird in self.age gespeichert
    def calcAge(self):
        pass  # entfernen




    def __str__(self):
        #ToDo
        pass

def main():
    kontaktListe = []
    # Datei öffnen und Json-Daten einlesen und speichern, etc.
    #ToDO





    print(f'Verbindung zu Server aufbauen ..')
    #Client Verbindung aufbauen; Socket wird erstellt; Socket in client_socket zuweisen
    #ToDo

    # Verbinden (connect) Sie sich mit dem Socket zu '127.0.0.1', Port 4444
    #ToDo


    print('Liste an Server senden')
    #ToDo unteren send Befehl auskommentieren
    #client_socket.send(pickle.dumps(austriaVIPList))       #genauso senden und Ergebnis beim Serveroutput kontrollieren
    #print('sent!')

if __name__ == '__main__':
    main()