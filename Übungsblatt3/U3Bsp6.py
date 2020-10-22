"""
Gregor Wagner
U3Bsp6.py - Klassen Kreis, Rechtek, Quadrat mit Methoden
Gregor Wagner, 52005240
"""
from cmath import pi as pi

class Kreis:
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        f = self.radius * self.radius * pi
        return round(f, 2)

    def umfang(self):
        u = 2 * self.radius * pi
        return round(u, 2)

    def __str__(self):
        return f"Kreis: \t\tFläche: {self.flaeche()}, Umfang: {self.umfang()}"

class Rechteck:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def flaeche(self):
        f = self.a * self.b
        return round(f, 2)

    def umfang(self):
        u = 2 * (self.a + self.b)
        return round(u, 2)

    def __str__(self):
        return f"Rechteck: \tFläche: {self.flaeche()}, Umfang: {self.umfang()}"

class Quadrat:
    def __init__(self, a):
        self.a = a

    def flaeche(self):
        f = self.a * self.a
        return round(f, 2)

    def umfang(self):
        u = 4 * self.a
        return round(u, 2)

    def __str__(self):
        return f"Quadrat: \tFläche: {self.flaeche()}, Umfang: {self.umfang()}"



def main() :
    k1 = Kreis(7.1)
    k2 = Kreis(4.8)
    r1 = Rechteck(3.1, 7.4)
    q1 = Quadrat(6)

    print(k1)
    print(k2)
    print(r1)
    print(q1)


if __name__ == "__main__":
    main()
