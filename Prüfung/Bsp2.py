"""
Author: Gregor Wagner
Bsp2 - client
Matr-Nr: 52005240
"""
import pickle,socket       # wird für s.send verwendet
import json
import datetime, time

class Kontakt():
    kontaktListe = []

    def __init__(self, id, vname, lname, birthday, country, vip):
        #ToDo  -> Werte zuweisen; vorher normalisieren (alles groß/klein schreiben, etc.)
        self.id = id
        self.vname = vname.capitalize()
        self.lname = lname.capitalize()
        self.birthday = birthday
        self.country = country.capitalize()
        self.vip = vip
        self.age = self.calcAge()

    # Alter berechnen und zurückgeben; wird in self.age gespeichert
    def calcAge(self):
        datetime_birthday = datetime.datetime.strptime(self.birthday,"%Y-%m-%d")
        datetime_now = datetime.datetime.now()
        datetime_age = datetime_now - datetime_birthday
        return int(datetime_age.days / 365.25)

    def importJson(filename):
        with open(file=filename, mode="r", encoding="utf-8") as kontakte_tmp :
            kontakte_tmp = json.load(kontakte_tmp)
            kontakte_tmp = kontakte_tmp['contacts']
        for k in kontakte_tmp :
            Kontakt.kontaktListe.append(Kontakt(k["id"], k['fname'], k['lname'], k['birthday'], k['country'], k['vip']))

    def remove_underage():
        for k in Kontakt.kontaktListe :
            if k.age < 18 :
                print(f"Removing person with ID: {k.id} - age: {k.age}") 
        tmp = list(filter(lambda x: x.age >= 18, Kontakt.kontaktListe))
        Kontakt.kontaktListe = tmp

    def getVIPlist():
        print("Österreicher mit VIP-Status")
        vipListe = []
        for k in sorted(filter(lambda x: x.vip == True and x.country == "Austria", Kontakt.kontaktListe),key=lambda x: x.age, reverse=True) :
            vipListe.append(k)
            print(k)
        return vipListe

    def __str__(self):
        return f"{self.id}: {self.vname} {self.lname} \t{self.birthday} \t\t {self.age} Jahre VIP: {self.vip} aus {self.country}"

def main():
    # Kontakt.importJson("python_homework/Prüfung/contacts.json")
    
    # Version 2
    # --------------------------------------------------------    
    Kontakt.importJson("contacts.json")
    Kontakt.remove_underage()
    
    print(f"\nAnzahl ohne minderjährige Kontakte {len(Kontakt.kontaktListe)}\n")

    austriaVIPList = Kontakt.getVIPlist()



    # Version 1
    #-----------------------------------------------------------
    # kontaktListe = []
    # # Datei öffnen und Json-Daten einlesen und speichern, etc.
    # with open("contacts.json", mode="r", encoding="utf-8") as contacts_data :
    #     kontakte_tmp = json.load(contacts_data)
    # kontakte_tmp = kontakte_tmp["contacts"]
    # for i,k in enumerate(kontakte_tmp) :
    #     kontaktListe.append(Kontakt(k["id"], k['fname'], k['lname'], k['birthday'], k['country'], k['vip']))
    #     if kontaktListe[i].age < 18:
    #         print(f"Removing person with ID: {kontaktListe[i].id} - age: {kontaktListe[i].age}") 
    # kontaktListe = list(filter(lambda x: x.age >= 18, kontaktListe))
    # print(f"\nAnzahl ohne minderjährige Kontakte {len(kontaktListe)}\n")

    # austriaVIPList = []
    # for k in sorted(filter(lambda x: x.vip == True and x.country == "Austria", kontaktListe),key=lambda x: x.age, reverse=True) :
    #     austriaVIPList.append(k)
    #     print(k)
    





    print(f'Verbindung zu Server aufbauen ..')
    #Client Verbindung aufbauen; Socket wird erstellt; Socket in client_socket zuweisen
    client_socket = socket.socket()

    # Verbinden (connect) Sie sich mit dem Socket zu '127.0.0.1', Port 4444
    client_socket.connect(("127.0.0.1",4444))


    print('Liste an Server senden')
    #ToDo unteren send Befehl auskommentieren
    client_socket.send(pickle.dumps(austriaVIPList))       #genauso senden und Ergebnis beim Serveroutput kontrollieren
    print('sent!')

if __name__ == '__main__':
    main()