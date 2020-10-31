"""
Gregor Wagner
U5Bsp2.py - Hangman
Gregor Wagner, 52005240
"""
import sys
import random

DEBUG = False

def usage():
    print("python U5Bsp.py <min-word-length> <max-word-length> <just Filename>")

def getRandomWord() :
    if len(sys.argv) == 4 :
        wordmin = int(sys.argv[1])
        wordmax = int(sys.argv[2])
        filename = sys.argv[3] + ".txt"
    elif DEBUG == True :
        wordmin = 3
        wordmax = 9
        filename = "python_homework/Übungsblatt5/country.txt"
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
    for w in word :
        solvedWord.append("-")
    fails = 0

    print("Welcome to my Hangman Game")
    while True :
        # show used Letters
        print(f"used letters: {sorted(list(set(usedLetters)))}")
        # show solved Part of the word: ---A-A-
        print(" ".join(solvedWord))

        # input
        guess = input("Guess your letter: ").upper()
        
        if guess in "".join(usedLetters) :
            print("Ooops! Already guessed that letter - try again")
            continue
        
        if len(guess) > 1 :
            if guess == "SOLVE" :
                solve = input("What is the word: ").upper()
                if solve == word :
                    print(f"Good job! You figured that the word is {solve.upper()}")
                    break
                else :
                    print(f"Sorry, that was not the word we are searching for.")
                    print(f"The Word was: {word}")
                    break
            if guess == "QUIT" :
                print(f"The word we were searching for was: {word}")
                break
        elif len(guess) == 1 :
            # print HIT or FAIL
            print("HIT" * (guess in word) + "FAIL" * (guess not in word))
        
            if guess in word :
                for i in range(len(word)) :
                    if guess == word[i] :
                        solvedWord[i] = word[i]
                if "".join(solvedWord) == word :
                    print(f"Congratulations, you found out that the word is {word}")
                    break
            else :
                fails += 1
                print(f"Fails: {fails}")

            if fails >= 10 :
                print(f"You had too many tries, maybe u get it next time.")
                print(f"The word we were searching for was: {word}")
                break

            usedLetters.append(guess)

if __name__ == "__main__":
    main()