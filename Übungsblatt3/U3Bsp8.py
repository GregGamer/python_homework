"""
Gregor Wagner
U3Bsp8.py - Wellnesscenter - ID Card
Gregor Wagner, 52005240
"""
import datetime

class IDCard :
    id = 0
    def __init__(self, name, birthday, credit) :
        IDCard.id += 1
        self.id = IDCard.id
        self.name = name
        self. birthday = birthday
        self.credit = credit
        datetime_birthday = datetime.datetime.strptime(birthday,"%d.%m.%Y")
        datetime_now = datetime.datetime.now()
        datetime_age = datetime_now - datetime_birthday
        self.age = int(datetime_age.days / 365.25)
        self.bookHistory = [credit]
        
    
    def chargeCredit(self,betrag) :
        if betrag >= 5 and (self.credit + betrag) <= 200 :
            self.credit += betrag
            self.bookHistory.append(betrag)
        else :
            print("Hopala, bei der Buchung gab es einen Fehler")
        return self.credit

    def bookService(self, services, extraServices) :
        if services == 0 or services == 2 :
            if self.age >= 18 :
                self.credit -= 25
                self.bookHistory.append(-25)
            else :
                self.credit -= 12
                self.bookHistory.append(-12)
        elif services == 1 :
            self.credit -= 18
            self.bookHistory.append(-18)
        else : 
            self.credit -= 25
            self.bookHistory.append(-25)

        if extraServices == 1 :
            self.credit -= 5
            self.bookHistory.append(-5)
        elif extraServices == 2 :
            self.credit -= 10
            self.bookHistory.append(-10)
        
        
    def __str__(self) :
        return f"ID: {self.id}, Name: {self.name}, Geburtstag/Alter: {self.birthday}/{self.age}, Guthaben: {self.credit}\nBookHistory: {self.bookHistory}"


def main() :
    i = 0
    personen = {} 
    for i in range(5) :
        personen[i] = IDCard(f"Person{i}", f"18.08.200{i}", i*10)
        print(personen[i])
    
    personen[0].chargeCredit(80)
    personen[0].bookService(0,2)
    personen[0].bookService(0,0)

    print(personen[0])



if __name__ == "__main__":
    main()