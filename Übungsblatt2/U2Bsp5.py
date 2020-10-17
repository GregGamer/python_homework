"""
Gregor Wagner
U2Bsp5 - Computer soll eine Zahl erraten
Gregor Wagner, 52005240
"""

inp = ""
count = 0

rangemin = 1
rangemax = 100


while 1 :
    guess = int((rangemin+rangemax)/2)

    print("computer guess:", guess)
    inp = input()

    if(inp != "richtig") :
        if(inp == "lower") :
            rangemax = guess
            count += 1
            continue
        elif(inp == "higher") :
            rangemin = guess
            count += 1
            continue
        else :
            continue
    else :
        print(f"correct - {count} attempts")
        break

