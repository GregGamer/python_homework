"""
Gregor Wagner
U3Bsp4.py - 
Gregor Wagner, 52005240
"""
import string
import random

def main() :
    passwordLen = 12
    passwordUp = 2
    passwordNum = 2
    passwordSign = 2
    i = 0
    password = ""

    while len(password) < passwordLen :
        for i in range(2) :
            if len(password) < passwordLen :
                password += random.choice(string.ascii_lowercase)
            
        for i in range(passwordUp) :
            if len(password) < passwordLen :
                password += random.choice(string.ascii_uppercase)
        
        for i in range(passwordNum) :
            if len(password) < passwordLen :
                password += random.choice(string.digits)
        
        for i in range(passwordSign) :
            if len(password) < passwordLen :
                password += random.choice(string.punctuation)
    
    l = list(password)
    random.shuffle(l)
    password = ''.join(l)

    print(f"Passwort: {password} \nLänge: {passwordLen}")



if __name__ == "__main__":
    main()