"""
Konsolenprogramm um mir die Übungsordnerstruktur zu erstellen
"""
import os
AUTHOR = "Gregor Wagner"
MATRNUM = "52005240"

def makeDirectory(uebungcount:int) :
    path = "Übungsblatt{}".format(uebungcount)
    os.mkdir(path)

def makeFiles(uebungcount, filecount) :
    filename = "U{}Bsp".format(uebungcount)
    path = "Übungsblatt{}/".format(uebungcount)

    for i in range(1, filecount+1) :
        curfilename = "{}{}.py".format(filename,str(i))
        with open(path + curfilename, "w+") as file:
            file.write("""\"""
{author}
{curfilename} - Uebungstitel
{author}, {matrnum}
""\"""".format(author=AUTHOR,curfilename=curfilename,matrnum=MATRNUM)
            )



def main() :
    uebungcount = input("Welche Übung ist es: ")
    filecount = int(input("Wie viele Files: "))
    
    makeDirectory(uebungcount)
    makeFiles(uebungcount, filecount)


main()