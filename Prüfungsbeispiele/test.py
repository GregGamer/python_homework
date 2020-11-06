liste1 = [1,2,3,4]
liste2 = [1,2,5]

ergebnis = [0,0,0,0]

gleicheElemente = set(liste1) & set(liste2)

print(gleicheElemente) #wichtig
print(len(gleicheElemente))

ergebnis[len(gleicheElemente)] += 1

print(ergebnis)