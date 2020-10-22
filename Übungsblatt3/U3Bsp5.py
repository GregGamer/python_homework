"""
Gregor Wagner
U3Bsp5.py - Passwort Hashen
Gregor Wagner, 52005240
"""
import hashlib

def hashPassword(password) :
    hash = hashlib.sha3_512(password.encode()).hexdigest()
    return hash


def main() :
    raw_Password1 = input("Please enter required password: ")
    hash_Password1 = hashPassword(raw_Password1)
    print(f"Hash: {hash_Password1}")
    raw_Password2 = input("Please enter required password: ")
    hash_Password2 = hashPassword(raw_Password2)
    print(f"Hash: {hash_Password2}")


    if hash_Password1 == hash_Password2 :
        print("Success - the entered passwords match.")
    else :
        print("Error - The passwords do not match.")


if __name__ == "__main__":
    main()