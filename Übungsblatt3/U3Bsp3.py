"""
Gregor Wagner
U3Bsp3.py - Lotto bis zum 6er
Gregor Wagner, 52005240
"""
import random
import time

def getRandomSample() :
    return random.sample(range(1,46),6)

startTime = time.time()
startNumbers = getRandomSample()
equal = 0
counter = 0
randomNumbers = []

while equal < 5:
    randomNumbers = getRandomSample()
    counter += 1
    equal = len(set(startNumbers) & set(randomNumbers))
    endTime = time.time()

takenTime = round(endTime-startTime, 2)
print(f"Ihre Gewinnerzahlen: {startNumbers} = {randomNumbers} \t Versuche: {counter} \nTime: {takenTime}s")