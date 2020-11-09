"""
Author: Gregor Wagner
Bsp1 - product quality
Matr-Nr: 52005240
"""
import random

class Produkt():
    ID = 1
    def __init__(self, quality, vulnerable, category, cost):
        self.id = Produkt.ID
        Produkt.ID += 1
        self.quality = round(quality,2)
        self.vulnerable = vulnerable
        self.category = category
        self.cost = round(cost,2)

    def __str__(self):
        return f"ID: {self.id} Quality: {self.quality}% Vulnerable: {self.vulnerable} Category: {self.category} Cost: {self.cost}€"

# ich wollte dieses Beispiel auch ändern wie in bsp2 aber leider blieb dafür keine Zeit mehr.
# ich hoffe es funktioniert trotzdem alles wie es soll

produkte = []
category = ["IT-Equipment", "Mobile", "Flight-Control", "Industrial-Part"]
for _ in range(15) :
    produkte.append(Produkt(random.uniform(20,100), random.choice([True, False]), random.choice(category), random.uniform(1000,3000)))

good_products = []
for i,p in enumerate(produkte) :
    if p.quality > 65 and p.vulnerable == False :
        good_products.append(p)
    else :
        print(f"removing product with ID {p.id} | {p.quality}, {p.vulnerable}")

noProductsLeft = False
print("\n\nProdukte mit niedrigster Qualität")
for g in sorted(good_products, key=lambda x: x.quality)[:5] :
    if g != None :
        print(g)
    else :
        noProductsLeft = True

if noProductsLeft :
    print("Kein Produkt mit den Kriterien vorhanden")

print("\n\nProdukte in Kategorie IT-Equipment oder Industrial-Part und mit Kosten von >= 2200€")
for g in sorted(good_products, key=lambda x: x.quality) :
    if (g.category == "IT-Equipment" or g.category == "Industrial-Part") and g.cost >= 2200 and g != None :
        print(g)
    else :
        noProductsLeft = True

if noProductsLeft :
    print("Kein Produkt mit den Kriterien vorhanden")
    
print(f"\nVerbleibende Produkte: \nAmount: {len(good_products)}")