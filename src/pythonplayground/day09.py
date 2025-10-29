# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

# inheritance in Python


class Student:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return "Student: " + self.firstname + " " + self.surname


class WorkingStudent(Student):  # extend class Student
    def __init__(self, firstname, surname, company):
        super().__init__(firstname, surname)  # call constructor of parent class
        self.company = company

    def name(self):  # overwrite Student.name()
        return super().name() + " (" + self.company + ")"  # call name() of parent class


student = WorkingStudent("Nils", "Holgerson", "Flugschule Wildgans")
print(student.name())

print("→---←")

students = {
    WorkingStudent("Ernst", "Haft", "Stadtverwaltung Musterstadt"),
    Student("Max", "Mustermann"),
    WorkingStudent("Jim", "Panse", "Zoo Musterstadt"),
    Student("Sabine", "Saubermann"),
}

for student in students:
    print(student.name())


# Fazit:
#
# ChildClass(ParentClass):
# how to extend a class
#
# super().functionName():
# how to call a function from the parent class
# example: super().__init__()
#
