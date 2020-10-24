"""
Gregor Wagner
U4Bsp2.py - 
Gregor Wagner, 52005240
"""
from collections import Counter

def main() :
    data = []
    
    f = open("einkaufsliste.txt", mode="r", encoding="utf-8")
    
    for x in f:
        x = x.replace("\n", "")
        print(x)
        data.append(x)

    f.close()

    for key, value in Counter(data).items() :
        print(f"{value}x -> {key}")


if __name__ == "__main__":
    main()