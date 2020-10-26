"""
Gregor Wagner
U4Bsp5.py - Fahrzeug vergleich mit csv datei einlesen
Gregor Wagner, 52005240
"""
import random
import operator

class Vehicle():
    def __init__(self, name, price, engine_size, cyl, hp, city_mpg, hwy_mpg, weight, length, width):
        self.name = name
        self.price = price
        self.engine_size = engine_size
        self.cyl = cyl
        self.hp = hp
        self.city_mpg = city_mpg
        self.hwy_mpg = hwy_mpg
        self.weight = weight
        self.length = length
        self.width = width
        self.cnt_wins = 0

        self.attr = ['name', 'price', 'engine_size', 'cyl', 'hp', 'city_mpg', 'hwy_mpg', 'weight', 'length', 'width']

    def vergleichsspiel(self, other):
        attr = random.choice(self.attr)
        if self.__getattribute__(attr) > other.__getattribute__(attr):
            self.cnt_wins += 1
        else :
            other.cnt_wins += 1

    def __str__(self) :
        return f"Name: {self.name} \t|| Price: {self.price} \t|| Wins: {self.cnt_wins}"

def readCSV(file) :
    f = open(file, mode="r", encoding="utf-8")
    data = f.read()
    f.close()
    return data

def loadDataIntoObject(data) :
    
    line = data.split("\n")
    line.remove(line[0])

    cars = []
    for l in line :
        c = l.split(";")
        cars.append(Vehicle(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9]))

    return cars

def main():
    carData = readCSV("vehicle.csv")

    vehicles = loadDataIntoObject(carData)
    
    for i in range(10000) :
        random.choice(vehicles).vergleichsspiel(random.choice(vehicles))

    vehiclesSorted = sorted(vehicles, key=operator.attrgetter("cnt_wins"))
    vehiclesSorted.reverse()
    print("Fahrzeuge mit mehr als 40 Siege:")
    for car in vehiclesSorted :
        if car.cnt_wins >= 40 :
            print(car)




if __name__ == "__main__":
    main()