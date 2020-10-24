"""
Gregor Wagner
U4Bsp3.py - 
Gregor Wagner, 52005240
"""
import json

class Person() :
    def __init__(self, v_name, l_name, city, post_code) :
        self.vname = v_name
        self.nname = l_name
        self.city = city
        self.post_code = post_code

    def __str__(self) :
        return f"{self.vname} {self.nname}, {self.post_code} {self.city}"


def getJsonFromFile(file) :
    f = open(file, mode="r", encoding='utf-8')
    data = f.read()
    f.close()

    return data

def checkPeople(people) :
    for i in people :
        print(i)
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
    print(people)

    print(f"\nEndgültige Anzahl d. Personen: {len(people)}")
    # for p in people :
        # print(p)

if __name__ == "__main__":
    main()