"""
https://mockaroo.com/
"""
import json
import random

with open('python_homework/Prüfungsbeispiele/students.json', mode="r", encoding="utf-8") as file :
    student_data = json.load(file) #unsere liste aus dictionaries


class Student():
    def __init__(self, vname, nname, mail):
        self.vname = vname
        self.nname = nname
        self.mail = mail
        self.exercise_grade = random.randint(45,100)
        self.exam_grade = random.randint(45,100)
        self.overall_grade = (self.exercise_grade+self.exam_grade)/2
        self.fail = random.randint(0,49)
        # self.fail

    def __str__(self):
        return f'Vorname: {self.vname}, Nachname: {self.nname}, Email: {self.mail}, Overall Grade: {self.exercise_grade}% | {self.exam_grade}% = {self.overall_grade}%'

    def __repr__(self):
        return f'Vorname: {self.vname}, Nachname: {self.nname}, Email: {self.mail}, Overall Grade: {self.overall_grade}%'



students = [] #das sollte eine Liste von Objekten sein
for s in student_data:
    # print(s['first_name'])
    students.append(Student(s['first_name'], s['last_name'], s['email'])) #so ruft man den wert von dictonary auf
   
# lambda asdf: asdf.overall_grade
# 
# sorted(students) # beim sorted wird die liste sortiert aber nur beim ausführen. Die originale liste bleibt unberührt
# students.sort()         #methode von einer list, mit sort wird die liste sortiert und bleibt auch so

students.sort(key=lambda x: x.overall_grade, reverse=True)
print("Best Students: ") # alles, was nur einmal ausgegeben sein sollte muss von der Schleife stehen
for s in students[:5]:
    print(s)

print("\nFails: ")
failed_students = []
for s in students:
    if s.exam_grade < 50 or s.exercise_grade < 50 :
        print(s)
        failed_students.append(s)

print(f'Endgültige Anzahl von Fail: {len(failed_students)}')

# print(students)

# (45 + 53) / 2 = 49