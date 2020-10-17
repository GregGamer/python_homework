"""
Gregor Wagner
U1Bsp6 - Passwort abfrage
Gregor Wagner, 52005240
"""
passwort = "bis"
i = 0

while i < 5 :
    passwd = input()
    if passwd == passwort :
        print("Login erfolgreich")
        break
    elif len(passwd) <= 0:
        continue
    else:
        i += 1
else :
    print("Login gesperrt")
