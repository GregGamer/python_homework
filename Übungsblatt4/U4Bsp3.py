"""
Gregor Wagner
U4Bsp3.py - 
Gregor Wagner, 52005240
"""
import json

class Person() :
    def __init__(self, v_name, l_name, city, post_code) :
        self.vname = v_name.capitalize()
        self.nname = l_name.capitalize()
        self.city = city.capitalize()
        self.post_code = post_code

    def __str__(self) :
        return f"{self.vname} {self.nname}, {self.post_code} {self.city}"


def getJsonFromFile(file) :
    try:
        f = open(file, mode="r", encoding='utf-8')
        data = f.read()
        f.close()
    except FileNotFoundError:
        print("Du bist vermutlich im Falschen Verzeichnis")
        exit()
    

    return data

def checkPeople(people) :
    
    for p1 in people :
        if p1.vname == "" or p1.nname == "" or p1.city == "" or p1.post_code == "":
            print(f'EMPTY ATTRIBUTES {p1}')
            people.remove(p1)
        p_gleich = 0
        if p1.vname == "Holly" :
            pass
        for p2 in people :
            if p1.vname == p2.vname and p1.nname == p2.nname and p1.city == p2.city and p1.post_code == p2.post_code :
                p_gleich += 1
                if p_gleich > 1 :
                    print(f"DUPLICATE {p2}")
                    people.remove(p2)

    for p in people :
        if p.vname == "" or p.nname == "" or p.city == "" or p.post_code == "":
            print(f'EMPTY ATTRIBUTES {p}')
            people.remove(p)



    return people    


def main() :
    json_data = getJsonFromFile("people.json")

    data = json.loads(json_data)
    data = data["people"]

    people = []
    for date in data :
        people.append(Person(date["v_name"], date["l_name"], date["city"], date["post code"]))
    # print(people[0])

    print(f"Anzahl d. eingelesenen Personen: {len(people)}")
    people = checkPeople(people)

    print(f"\nEndgültige Anzahl d. Personen: {len(people)}")
    for p in people :
        print(p)

if __name__ == "__main__":
    main()