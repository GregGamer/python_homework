import json, random

class Student() :
    def __init__(self, vname, nname, mail) :
        self.vname = vname
        self.nname = nname
        self.mail = mail
        self.exam_grade = random.randint(45,100)
        self.exercise_grade = random.randint(45,100)
        self.overall_grade = self.exam_grade * 0.5 + self.exercise_grade * 0.5

    def __str__(self) :
        return f"Name: {self.vname} {self.nname}\t Exercise: {self.exercise_grade}%\t Exam: {self.exam_grade}%\t Overall: {self.overall_grade}%"

class Students() :
    def __init__(self, students_data) :
        f = open(students_data, mode="r", encoding="utf-8")
        file_data = json.load(f)
        f.close()
        self.students = []
        for f in file_data :
            self.students.append(Student(f['first_name'], f['last_name'], f['email']))
        
    
    def printBestStudents(self) :
        print("Best Students: ")
        for s in sorted(self.students, key= lambda s: s.overall_grade, reverse=True)[:5] :
            print(s)
        print("")

    def printFailClass(self) :
        print("Failed Students: ")
        failed_students = list(filter(lambda s: s.exam_grade < 50 or s.exercise_grade < 50, self.students))
        for s in failed_students :
            print(f"FAILED CLASS -> {s}")
        print(f"Insgesamt sind {len(failed_students)} Studierende negativ")
        print("")



def main() :
    students = Students("python_homework/Prüfungsbeispiele/students.json")

    students.printBestStudents()

    students.printFailClass()




if __name__ == "__main__":
    main()