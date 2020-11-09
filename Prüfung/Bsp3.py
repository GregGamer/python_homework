"""
Author: Gregor Wagner
Bsp3 - ich hab mein Lotto komplett neu geschrieben, ist einfacher so
Matr-Nr: 52005240
"""
import random

money = 3500
bidding_costs = [0,0,0,5.5,55,2500,1000000]
tip_cost = 1.5
my_tip = random.sample(range(1,46),6)
erg = [0] * 7

counter = 0
while money >= tip_cost:
    money -= tip_cost
    random_tip = random.sample(range(1,46),6)
    count_equal_tipps = len(set(my_tip)&set(random_tip))
    money += bidding_costs[count_equal_tipps]
    erg[count_equal_tipps]+=1
    counter += 1

for i,e in enumerate(erg) :
    print(f"{i}er: {e}")
print(f"Du hast {counter} mal gespielt")