"""
Gregor Wagner
U3Bsp7.py - Personen Klassen
Gregor Wagner, 52005240
"""
import datetime
import time

class Person :
    def __init__(self, name, birthday, plzcode) :
        self.name = name
        self.birthday = birthday
        self.plzcode = plzcode
        datetime_birthday = datetime.datetime.strptime(birthday,"%d.%m.%Y")
        datetime_now = datetime.datetime.now()
        datetime_age = datetime_now - datetime_birthday
        self.age = int(datetime_age.days / 365.25)


    def __str__(self) :
        return f'{self.name}, geboren am {self.birthday}, wohnhaft in {self.plzcode} ist {self.age} Jahre alt.'



def main() :
    p1 =Person('Alfred Maurer','08.06.2001',3100)
    p2 =Person('Lisa Winkler','22.05.1992',1100)
    p3 =Person('Ernst Hindler','01.10.1919',1120)

    print(p1)
    print(p2)
    print(p3)


if __name__ == "__main__":
    main()