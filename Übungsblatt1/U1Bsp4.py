"""
Gregor Wagner
U1Bsp4 - Rabatt berechnen
Gregor Wagner, 52005240
"""

money = int(input("Betrag (€): "))

if(money < 1000) :
    money *= 0.95
    print(f"Zahlungsbetrag: {money}€")

if(1000 <= money < 2000) :
    money *= 0.9
    print(f"Zahlungsbetrag: {money}€")

if(2000 <= money < 5000) :
    money *= 0.85 
    money *= 0.98 
    print(f"Zahlungsbetrag: {money}€")

if(5000 <= money) :
    money *= 0.8
    money *= 0.97
    print(f"Zahlungsbetrag: {money}€")
