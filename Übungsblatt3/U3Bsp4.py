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
    passwordLow = 2
    passwordNum = 2
    passwordSign = 2

    password = random.choices(string.ascii_lowercase,k=passwordLow)
    password += random.choices(string.ascii_uppercase,k=passwordUp)
    password += random.choices(string.digits,k=passwordNum)
    password += random.choices(string.punctuation,k=passwordSign)

    everyletter = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(everyletter,k=passwordLen-len(password))

    tmp = [*password]
    random.shuffle(tmp)
    password = ''.join(tmp)

    print(f"Passwort: {password} \nLänge: {passwordLen}")



if __name__ == "__main__":
    main()