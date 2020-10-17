"""
Gregor Wagner
U2Bsp2 - Palindrom
Gregor Wagner, 52005240
"""

string = input("Wort eingeben: ").lower()
reverse = string[::-1]

if string == reverse :
    print("True")
else : 
    print("False")