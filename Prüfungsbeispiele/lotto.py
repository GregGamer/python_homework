"""
Lotto
"""
import random
import collections

tip_input = map(int, input("tip input: ").split())          # [1, 2, 5, 20, 10, 43,]
draw_count = int(input('Draw count: '))

ergebnis = [0, 0, 0, 0, 0, 0, 0]
for i in range(draw_count):
    gewinner_zahlen = random.sample(range(1,46), 6)
    gleicheElemente = len(set(tip_input) & set(gewinner_zahlen))
    ergebnis[gleicheElemente] += 1


print(f"0er: {ergebnis[0]}")
print(f"1er: {ergebnis[1]}")
print(f"2er: {ergebnis[2]}")
print(f"3er: {ergebnis[3]}")
print(f"4er: {ergebnis[4]}")
print(f"5er: {ergebnis[5]}")
print(f"6er: {ergebnis[6]}")
