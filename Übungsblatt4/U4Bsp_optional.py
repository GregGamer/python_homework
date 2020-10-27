"""
Gregor Wagner
U4Bsp_optional.py - Consolen Programm - Bug/Issue Tracker
Gregor Wagner, 52005240
"""
# TODO - color Coding, alle Inputs grün, IDs rot, verfügbare Befehle blau, offene Events gleb und geschlossene schwarz, bei den Events ein color Coding je nach prio
import time

class Event():
    eid = 0
    def __init__(self, reporter, title, description, priority) :
        self.eid = Event.eid
        Event.eid += 1
        self.reporter = reporter
        self.title = title
        self.description = description
        self.priority = priority
        self.timestamp = time.time()
        self.isOpen = True

    def __str__(self):
        return f"\033[0;31;40m{self.eid}\033[0;33;40m, {self.title}, gemeldet von: {self.reporter}, ist offen {self.isOpen}, Prio: {self.priority}\033[0;37;40m"

class Bug(Event):
    def __init__(self, reporter, title, description, priority, gitHash) :
        super().__init__(reporter, title, description, priority)
        self.gitHash = gitHash

    def getGitHash(self):
        return self.gitHash

    def setGitHash(self, gitHash):
        self.gitHash = gitHash

class Incident(Event):
    def __init__(self, reporter, title, description, priority, cve):
        super().__init__(reporter, title, description, priority)
        self.cve = cve
    
    def getCve(self) :
        return self.cve

    def setCve(self, cve) : 
        self.cve = cve

class Person():
    pid = 0
    def __init__(self, name, email):
        self.pid = Person.pid
        Person.pid += 1
        self.name = name
        self.email = email

    def __str__(self):
        return f"\033[0;31;40m{self.pid}\033[0;33;40m, Name: {self.name}, Email: {self.email}\033[0;37;40m"

# Klassen Ende =========================================

def newPerson(eventListe, personenListe):
    name = input("Name --> ")
    mail = input("E-Mail --> ")

    error = False
    try:
        personenListe.append(Person(name,mail))
    except:
        error = True

    if error :
        print("Person wurde NICHT hinzugefügt, es gab einen Fehler")
        return personenListe
    print("Person erfolgreich hinzugefügt")
    return personenListe

def listPersons(eventListe, personenListe):
    print("Personen")
    print("--------")
    for p in personenListe :
        print(p)

def newBug(eventListe, personenListe):
    if len(personenListe) == 0 :
        print("Es muss zuerst eine Person angelegt werden")
        newPerson(eventListe, personenListe)

    print("Wer hat den Bug gemeldet?\n")
    for p in personenListe :
        print(p)
    
    #TODO - try catch über die inputs und abfrage ob die eingegebene pid auch existiert
    pid = int(input("--> "))

    print(f"Reporter: {personenListe[pid].name}")
    titel = input("Titel --> ")
    description = input("Description --> ")
    priority = int(input("Priorität [0-10] --> "))
    gitHash = input("Git-Commit-Hash --> ")

    eventListe.append(Bug(personenListe[pid], titel, description,priority, gitHash))

    return eventListe

def newIncident(eventListe, personenListe):
    if len(personenListe) == 0 :
        print("Es muss zuerst eine Person angelegt werden")
        newPerson(eventListe, personenListe)

    print("Wer hat den Incident gemeldet?\n")
    for p in personenListe :
        print(p)
    

    #TODO - try catch über die inputs und abfrage ob die eingegebene pid auch existiert
    pid = int(input("--> "))

    print(f"Reporter: {personenListe[pid].name}")
    titel = input("Titel --> ")
    description = input("Description --> ")
    priority = int(input("Priorität [0-10] --> "))
    cve = input("CVE --> ")

    eventListe.append(Incident(personenListe[pid], titel, description, priority, cve))

    return eventListe

def listEvents(eventListe, personenListe):
    print("Events")
    print("------")
    for e in eventListe : 
        if e.isOpen == True :
            print(e)

def closeEvent(eventListe, personenListe):
    for e in eventListe :
        if e.isOpen == True :
            print(e)

    # TODO - try catch und überprüfen ob der input auch existiert
    eid = int(input("--> "))

    eventListe[eid].isOpen = False

    print("Event wurde geschlossen!")


def listCommands(commands):
    # TODO - verbesserte Art commands hinzuzufügen, mybe via dictionary
    
    commandString = " | ".join(list(commands.keys()))

    print(f"\033[1;34;40mBefehle: exit | {commandString}\033[0;37;40m")



def main() :

    personenListe = []
    eventListe = []
    
    commands = {"new person"    : newPerson, 
                "list persons"  : listPersons, 
                "new bug"       : newBug, 
                "new incident"  : newIncident, 
                "list events"   : listEvents, 
                "close events"  : closeEvent}

    while (consoleLog := input("--> ")) != "exit" :
        command = consoleLog.lower()
        for key, value in commands.items() :
            if command == key.lower() :
                value(eventListe, personenListe)
        listCommands(commands)


if __name__ == "__main__":
    main()