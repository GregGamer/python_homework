"""
Gregor Wagner
U5Bsp2.py - Hangman
Gregor Wagner, 52005240
"""
import sys
import random

def usage():
    print("python U5Bsp.py <min-word-length> <max-word-length> <just Filename>")

def getRandomWord() :
    if len(sys.argv) == 4 :
        wordmin = int(sys.argv[1])
        wordmax = int(sys.argv[2])
        filename = sys.argv[3] + ".txt"
    else :
        usage()
        quit()

    f = open(filename, mode="r", encoding="utf-8")

    wordlist = []
    for w in f :
        w = w.replace("\n", "")
        if wordmin <= len(w) <= wordmax :
            wordlist.append(w)
    
    f.close()

    randomWord = random.choice(wordlist)
    return randomWord.upper()

def main() :
    word = str(getRandomWord())
    usedLetters = list()
    solvedWord = []
    fails = 0

    for w in word :
        solvedWord.append("-")

    print("Welcome to my Hangman Game")
    while True :
        print(" ".join(solvedWord))
        guess = input("Guess your letter: ").upper()
        usedLetters.append(guess)
        if guess in word:
            print("HIT")
            for i in range(len(word)) :
                if guess == word[i] :
                    solvedWord[i] = word[i]
        else:
            if guess not in usedLetters :
                fails += 1
            print(f"FAIL: {fails}")
            if fails >= 10 :
                print("Nicht geschafft")
                quit()
        print(f"used letters: {sorted(list(set(usedLetters)))}")

        if "-" not in solvedWord :
            solve = "".join(solvedWord)
            print(f"solved\nWhat is the word: {word}\nGood job! You figured that the word is {solve}")
            quit()



if __name__ == "__main__":
    main()