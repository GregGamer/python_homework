"""
Gregor Wagner
U4Bsp1.py - 
Gregor Wagner, 52005240
"""
import datetime
from collections import Counter

class Person() :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) :
        return f"Name: {self.name}, Alter: {self.age}"

class LehrerIn(Person) :
    def __init__(self, name, age, school, classes):
        super().__init__(name, age)
        self.school = school
        self.classes = classes

    def __str__(self) :
        return f"Name: {self.name}, Alter: {self.age}, Schule: {self.school}, {self.classes}"


class SportlerIn(Person):
    def __init__(self, name, age, sportart, rank):
        super().__init__(name, age)
        self.sportart = sportart
        self.rank = rank

    def __str__(self) :
        return f"Name: {self.name}, Alter: {self.age}, Sportart: {self.sportart}, Rangliste: {self.rank}"


class SkifahrerIn(SportlerIn):
    def __init__(self, name, age, sportart, rank, wins):
        super().__init__(name, age, sportart, rank)
        self.wins = wins

    def __str__(self) :
        return f"Name: {self.name}, Alter: {self.age}, Sportart: {self.sportart}, Rangliste: {self.rank}, Siege: {self.wins}"
def main() :

    tina = SkifahrerIn('Tina', 18, 'skifahren', 2, 15)
    print(tina)
    print(type(tina))
    
    max = SportlerIn('Max', 20, 'Tennis', 200)
    print(max)
    print(type(max))
    
    moritz = LehrerIn('Moritz', 45, 'Real Gymnasium', 5)
    print(moritz)
    print(type(moritz))



if __name__ == "__main__":
    main()