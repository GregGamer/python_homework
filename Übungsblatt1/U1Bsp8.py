"""
Gregor Wagner
U1Bsp7 - EURO Scheine
Gregor Wagner, 52005240
"""
euro = int(input("Input (Euro): "))
notes = [500,200,100,50,20,10,5,2,1]

erg = "Resultat: "
notes = sorted(notes,reverse=True)

for note in notes:
    if euro >= note :
        temp = int(euro / note)
        euro = euro % note
        erg += '{temp} x {note}-Euro-Scheine, '.format(temp=temp,note=note)

print(erg)