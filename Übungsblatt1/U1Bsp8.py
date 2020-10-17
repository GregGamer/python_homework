"""
Gregor Wagner
U1Bsp7 - EURO Scheine
Gregor Wagner, 52005240
"""
euro = int(input("Input (Euro): "))

erg = "Resultat: "

if euro >= 500 :
    temp = int(euro / 500)
    euro = euro % 500
    erg += str(temp) + " x 500-Euro-Scheine, "

if euro >= 200 :
    temp = int(euro / 200)
    euro = euro % 200
    erg += str(temp) + " x 200-Euro-Scheine, "

if euro >= 100 :
    temp = int(euro / 100)
    euro = euro % 100
    erg += str(temp) + " x 100-Euro-Scheine, "

if euro >= 50 :
    temp = int(euro / 50)
    euro = euro % 50
    erg += str(temp) + " x 50-Euro-Scheine, "

if euro >= 20 :
    temp = int(euro / 20)
    euro = euro % 20
    erg += str(temp) + " x 20-Euro-Scheine, "

if euro >= 10 :
    temp = int(euro / 10)
    euro = euro % 10
    erg += str(temp) + " x 10-Euro-Scheine, "

if euro >= 5 :
    temp = int(euro / 5)
    euro = euro % 5
    erg += str(temp) + " x 5-Euro-Scheine, "

if euro >= 2 :
    temp = int(euro / 2)
    euro = euro % 2
    erg += str(temp) + " x 2-Euro-Münze, "

if euro >= 1 :
    temp = int(euro / 1)
    euro = euro % 1
    erg += str(temp) + " x 1-Euro-Münze, "

print(erg)