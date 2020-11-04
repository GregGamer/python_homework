"""
Prüfungsbeispiel 1 - Klasse Mitarbeiter mit Methoden
Author: Gregor und Magda

Links:
https://docs.python.org/3/library/random.html

"""
import random

class Mitarbeiter:
    def __init__(self, name, gehalt, freunde, abteilung) :
        self.name = str(name)
        self.gehalt = round(float(gehalt),2)
        self.lieblings_kollegen = list(freunde)
        self.abteilung = str(abteilung)

    def __str__(self) :
        return f'Name: {self.name}, Gehalt: {self.gehalt}, Abteilung:{self.abteilung}'

    def __repr__(self) :
        return f'Name: {self.name}, Gehalt: {self.gehalt}, Abteilung:{self.abteilung}'

    def gehalts_erhoehung(self):
        self.gehalt = self.gehalt * 1.2

    def addFreund(self, kollege):
        if kollege not in self.lieblings_kollegen:
            self.lieblings_kollegen.append(kollege) # füge ich den kollegen als freund hinzu
        if self not in kollege.lieblings_kollegen:
            kollege.lieblings_kollegen.append(self)

def main() :
    mitarbeiter_namen = ["Anton", "Bernd", "Carola", "David", "Ernst", "Fritz"]
    mitarbeiter_liste = []

    for name in mitarbeiter_namen:
        m1 = Mitarbeiter(name, random.randint(1500,2500), [], "Webdevelopment")
        mitarbeiter_liste.append(m1)
    
    print(mitarbeiter_liste[0].gehalt) #gehalt
    mitarbeiter_liste[0].gehalts_erhoehung() #gehalt wir erhöht
    print(mitarbeiter_liste[0].gehalt) # kommt gehalt mit erhöhung

    alle_mitarbeiter(mitarbeiter_liste) # damit geben wir der alle_mit liste die alle mitarbeiter weiter damit wir sie unten aufrufen können
    
    mitarbeiter_liste[0].addFreund(mitarbeiter_liste[1]) #freunde werde hinzugefügt        
    mitarbeiter_liste[0].addFreund(mitarbeiter_liste[2]) #freunde werde hinzugefügt
    mitarbeiter_liste[1].addFreund(mitarbeiter_liste[0]) #freunde werde hinzugefügt

    print(mitarbeiter_liste[0].lieblings_kollegen)
    print(mitarbeiter_liste[1].lieblings_kollegen)


def alle_mitarbeiter(mitarbeiter):
    for m in mitarbeiter:
        print(m)



if __name__ == "__main__":
    main()