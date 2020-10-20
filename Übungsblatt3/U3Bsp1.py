"""
Gregor Wagner
U3Bsp1.py - Exception handling
Gregor Wagner, 52005240
"""

def calculator :
    num1 = input("Please enter number: ")
    num2 = input("Another number: ")
    return

try:
    num3 = num1 / num2
except ZeroDivisionError as identifier:
    print("Falsche Eingaben -Versuch gescheitert!")
except ValueError as identifier:
    print("Falsche Eingaben -Versuch gescheitert!")