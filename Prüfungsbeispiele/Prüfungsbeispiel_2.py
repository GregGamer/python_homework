"""
https://mockaroo.com/
"""
import json

with open('python_homework/Prüfungsbeispiele/students.json', mode="r", encoding="utf-8") as file :
    student_data = json.load(file) #unsere liste aus dictionaries


class Student():
    def __init__(self, vname, nname, mail):
        self.vname = vname
        self.nname = nname
        self.mail = mail

    def __str__(self):
        return f'Vorname: {self.vname}, Nachname: {self.nname}, Email: {self.mail}'

    def __repr__(self):
        return f'Vorname: {self.vname}, Nachname: {self.nname}, Email: {self.mail}'



students = [] #das sollte eine Liste von Objekten sein
for s in student_data:
    # print(s['first_name'])
    students.append(Student(s['first_name'], s['last_name'], s['email'])) #so ruft man den wert von dictonary auf
    

for s in students :
    print(s)

# print(students)