"""
Gregor Wagner
U2Bsp3 - Listen
Gregor Wagner, 52005240
"""

a = [1, 1, 'hello', 'hello', 2, 5, 8, 13, 22, 2, 'world']
b = [55, 5, 1, 2, 2, 5]

c = set(a+b)
a = set(a)
b = b.sort()
b = set(b)

print(c)
print(a-b)
print(b)