"""
Gregor Wagner
U1Bsp5 - Rabatt berechnen
Gregor Wagner, 52005240
"""

string1 = input("String1: ")
string2 = input("String2: ")
index = int(input("Index: "))

if len(string1) >= index : 
    if string1[index-1] == string2[index-1] :
        print(string1[index-1].lower())
    else :
        print("ungleich")
else :
    print("ungleich")