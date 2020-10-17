"""
Gregor Wagner
U1Bsp7 - HIPP HOPP
Gregor Wagner, 52005240
"""
i = 0

for n in range(1,50) :
    string = ""
    if n % 3 == 0:
        string += "HIPP "
    if n % 5 == 0:
        string += "HOPP "
    if string != "" :
        print(f"{string}")
    if n == 19 :
        break