"""
Gregor Wagner
U2Bsp6 - count letters
Gregor Wagner, 52005240
"""

sentence = 'Jim quickly realized that the beautiful gowns are expensive'
sentence = sentence.replace(" ", "")
lettersDict = dict()
lettersList = [*sentence]


for n in lettersList :
    lettersDict[n] = lettersList.count(n)

print(lettersDict)