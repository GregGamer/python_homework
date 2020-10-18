"""
Gregor Wagner
U2Bsp6 - count letters
Gregor Wagner, 52005240
"""
def ConvertToString(sentence): 
    letters=[] 
    letters[:0]=sentence
    return letters 

sentence = 'Jim quickly realized that the beautiful gowns are expensive'
sentence = sentence.replace(" ", "")
lettersDict = dict()
lettersList = ConvertToString(sentence)


for n in lettersList :
    lettersDict[n] = lettersList.count(n)

print(lettersDict)