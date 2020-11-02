"""
Gregor Wagner
U4Bsp4.py - 
Gregor Wagner, 52005240
"""
import sys 

def usage():
    print("Falsche Parameter Eingabe")
    print("<myProgram.py> <arg1> <arg2>")

if len(sys.argv) == 3 :
    try :
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
    except ValueError :
        usage()

    # dreht zwei Variablen um
    if arg2 < arg1 :
        arg1, arg2 = arg2, arg1

    for i in range((arg2+1) - arg1) :
        print(i+arg1)

else :
    usage()
