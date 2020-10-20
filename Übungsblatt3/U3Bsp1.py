"""
Gregor Wagner
U3Bsp1.py - Exception handling
Gregor Wagner, 52005240
"""

def calculator() :
    try :
        num1 = int(input("Please enter number: "))
        num2 = int(input("Another number: "))
        num3 = num1 / num2
    except ZeroDivisionError :
        print("Falsche Eingaben -Versuch gescheitert!")
    except ValueError :
        print("Falsche Eingaben -Versuch gescheitert!")
    else : 
        print(f"{num1} / {num2} = {num3}")



def main() :
    calculator()

if __name__ == "__main__":
    main()