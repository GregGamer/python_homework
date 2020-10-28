"""
Gregor Wagner
U4Bsp_optional.py - Consolen Programm - Bug/Issue Tracker
Gregor Wagner, 52005240

Upate zum "alten" Programm:
    hinzugefügt:
        command: save file          //es ist jetzt möglich alle Daten die erstellt worden sind als file zu speichern
        command: load file          //es ist jetzt möglich die gespeicherten Daten zu laden und damit weiterzuarbeiten, [gibt noch kleine bugs]
        command: list all events     //weil "list events" nur die offenen bugs angezeigt hat
    Error handling bei falschen inputs
"""

import time
import json

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

    def jsonencode(self):
        return {"reporter": self.reporter.pid, "title": self.title, "description": self.description, "priority": self.priority, "isOpen": self.isOpen, "gitHash": self.gitHash}

class Incident(Event):
    def __init__(self, reporter, title, description, priority, cve):
        super().__init__(reporter, title, description, priority)
        self.cve = cve
    
    def getCve(self) :
        return self.cve

    def setCve(self, cve) : 
        self.cve = cve

    def jsonencode(self):
        return {"reporter": self.reporter.pid, "title": self.title, "description": self.description, "priority": self.priority, "isOpen": self.isOpen, "cve": self.cve}

class Person():
    pid = 0
    def __init__(self, name, email):
        self.pid = Person.pid
        Person.pid += 1
        self.name = name
        self.email = email

    def jsonencode(self):
        return {"name": self.name, "email":self.email}

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
    try:
        pid = int(input("--> "))
    except ValueError:
        print("Fehler")

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

def listAllEvents(eventListe, personenListe):
    print("Events")
    print("------")
    for e in eventListe : 
        print(e)

def closeEvent(eventListe, personenListe):
    for e in eventListe :
        if e.isOpen == True :
            print(e)

    # TODO - try catch und überprüfen ob der input auch existiert
    eid = int(input("--> "))

    eventListe[eid].isOpen = False

    print("Event wurde geschlossen!")

def saveFile(eventListe, personenListe):
    filename = input("Filename --> ") + ".json"
    f = open(filename, mode="w", encoding="utf-8")

    jsonList = {"personenListe": [], "eventListe": []}
    for p in personenListe :
        print(p.jsonencode())
        jsonList["personenListe"].append(p.jsonencode())

    for e in eventListe :
        print(e.jsonencode())
        jsonList["eventListe"].append(e.jsonencode())

    print(jsonList)
    f.write(json.dumps(jsonList))

    f.close()


def loadFile(eventListe, personenListe):
    filename = input("Filename --> ") + ".json"
    f = open(filename, mode="r", encoding="utf-8")

    jsonList = json.load(f)
    for p in jsonList["personenListe"] : 
        personenListe.append(Person(p['name'], p['email']))
    i = 0
    for e in jsonList['eventListe'] :
        if 'cve' in e :
            eventListe.append(Incident(personenListe[e['reporter']], e['title'], e['description'], e['priority'], e['cve']))
        elif 'gitHash' in e :
            eventListe.append(Bug(personenListe[e['reporter']], e['title'], e['description'], e['priority'], e['gitHash']))
        if e['isOpen'] == False :
            eventListe[i].isOpen = False
        i += 1
    


def listCommands(commands):
    commandString = " | ".join(list(commands.keys()))
    print(f"\033[1;34;40mBefehle: exit | {commandString}\033[0;37;40m")



def main() :

    personenListe = []
    eventListe = []
    
    commands = {"save file"     : saveFile,
                "load file"     : loadFile,
                "new person"    : newPerson, 
                "list persons"  : listPersons, 
                "new bug"       : newBug, 
                "new incident"  : newIncident, 
                "list events"   : listEvents, 
                "list all events": listAllEvents,
                "close events"  : closeEvent}

    while (consoleLog := input("--> ")) != "exit" :
        command = consoleLog.lower()
        for key, value in commands.items() :
            if command == key.lower() :
                value(eventListe, personenListe)
        listCommands(commands)


if __name__ == "__main__":
    main()