"""
Gregor Wagner
U3Bsp3.py - Lotto bis zum 6er
Gregor Wagner, 52005240
"""
import random
import time

def getRandomSample() :
    return random.sample(range(46),6)

def main() :
    startTime = time.time()
    startNumbers = getRandomSample()
    # startNumbers = [41,34,15,3,10,44]
    equal = 0
    counter = 0
    randomNumbers = []
    # money = 1000
    # price = [0,0,3,10,50,4000,800000]

    while equal != 4 or startNumbers == randomNumbers:
        randomNumbers = getRandomSample()
        # money -= 1
        counter += 1
        if startNumbers != randomNumbers :
            equal = len(set(startNumbers) & set(randomNumbers))
            # print(f"{startNumbers} != {randomNumbers} \t => equal = {equal} => {counter}    ")
        else :
            print("gleich")
        endTime = time.time()
        # money += price[equal]
    takenTime = round(endTime-startTime, 2)
    print(f"Ihre Gewinnerzahlen: {randomNumbers} \t Versuche: {counter} \nTime: {takenTime}s")
        # print(f"{counter} \t money = {money}")

if __name__ == "__main__":
    main()