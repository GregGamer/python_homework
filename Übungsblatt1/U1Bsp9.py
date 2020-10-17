"""
Gregor Wagner
U1Bsp9 - Fibonacci-Reihe
Gregor Wagner, 52005240
"""

z0 = 0
z1 = 1

for n in range(1,50) :
    print(f"{z0}, ")

    z2 = z0+ z1
    z0 = z1
    z1 = z2