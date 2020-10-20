"""
Gregor Wagner
U3Bsp2.py - Lotto mit Fehlerbehandlung
Gregor Wagner, 52005240
"""

import random

def checkTip(lottoTipp) :
    count = 0
    i = 0

    for i in set(lottoTipp) :
        if i > 45 :
            print("Eine Zahl ist zu hoch")
            count = 0
            lottoTipp = lottoInput()
        elif i < 1 :
            print("Eine Zahl ist zu klein")
            count = 0
            lottoTipp = lottoInput()
        else :
            count += 1

    if count < 6 :
        print("Input war zu kurz oder hatte gleiche Zahlen")
        lottoTipp = lottoInput()

    return lottoTipp


def lottoInput() :        
    try:
        lottoTipp = input("tip input: ")
        lottoTipp = lottoTipp.split(" ")
        for i in range(0,len(lottoTipp)) :
            lottoTipp[i] = int(lottoTipp[i])
    except ValueError:
        print("ERROR - Falscher Input")
        lottoInput()
    except TypeError:
        print("ERROR - Falscher Type")




    lottoTipp = checkTip(lottoTipp)

    return lottoTipp


def compareTipp(lottoTipp, drawCount) :
    wins = [0, 0, 0, 0, 0, 0, 0]
    equalTipps = 0
    i = 0
    n = 0

    for i in range(drawCount) :
        equalTipps = 0
        equalTippsSet = set(lottoTipp) & set(random.sample(range(1,46), 6))
        for n in equalTippsSet :
            equalTipps += 1
        wins[equalTipps] += 1
    
    return wins


def printWins(wins) :
    for i in range(len(wins)) :
        print(f'{i}er: {wins[i]}')


def main() :
  
    lottoTipp = lottoInput()
    # print(lottoTipp)

    drawCount = int(input("draw count: "))

    wins = compareTipp(lottoTipp, drawCount)

    printWins(wins)

main()