"""
Gregor Wagner
U2Bsp4 - Dictonary
Gregor Wagner, 52005240
"""

pets = {'cat': 4, 'dog': 15, 'bird': 5, 'velociraptor': 150}

pets["mouse"] = 1
pets["dog"] = 20
del pets["bird"]

for i in pets :
    print(f"{i}: {pets[i]}")