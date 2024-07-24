"""
Gregor Wagner
U2Bsp2 - Palindrom
Gregor Wagner, 52005240
"""

string = input("Wort eingeben: ").lower()
print(str(string == string[::-1]))