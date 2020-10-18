"""
Konsolenprogramm um mir die Übungsordnerstruktur zu erstellen
"""
import os

def makeDirectory(uebungcount) :
    path = "Übungsblatt"+uebungcount+""
    os.mkdir(path)


def makeFiles(uebungcount, filecount) :
    filename = "U"+uebungcount+"Bsp"
    path = "Übungsblatt"+uebungcount+"/"
    author = "Gregor Wagner"
    matrnum = "52005240"

    for i in range(1, filecount+1) :
        curfilename = filename + str(i) + ".py"
        f = open(path + curfilename, "w+")
        f.write(f"\"\"\"\n{author}\n{curfilename} - \n{author}, {matrnum}\n\"\"\"")
        f.close



def main() :
    uebungcount = input("Welche Übung ist es: ")
    filecount = int(input("Wie viele Files: "))
    
    makeDirectory(uebungcount)
    makeFiles(uebungcount, filecount)


main()