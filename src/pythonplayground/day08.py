# OOP in Python:
# private Eigenschaften, Methoden, special class methods


class UniversityRegister:

    def __init__(self):
        self.__students = {}

        # Konvertion unter Programmierern! Nicht Fest.
        # Variable/Methoden mit Unterstrich nicht von außen zugreifen.
        #
        # self._term = 1
        # self._do_something()

        self.__do_something()

    def __do_something(self):
        """demo - private methode"""
        print("Do Something!")

    def increase_student_term(self, name):
        """erhöhen des Semesters eines Studenten um 1"""
        if self.__students[name] >= 9:
            return
        self.__students[name] = self.__students[name] + 1

    def get_student_term(self, name):
        """gibt das Semester eines Studenten zurück"""
        return self.__students[name]

    def add_student(self, name):
        """für einen neuen Studenten hinzu"""

        if name in self.__students:
            return

        self.__students[name] = 1

    def get_student(self, name):
        """gibt einen Studenten zurück"""

        return self.__students[name]

    # #### SPECIAL METHODS ####

    def __repr__(self):
        """ special method """
        # it controls what is returned when the object is printed
        # in an unambiguous way, used for technical logging

        return str(self.__students)

    def __str__(self):
        """ special method """
        # it controls what is returned when the object is printed
        # in a readable way, used for 'user' output
        # uses __repr__() if no __str__() is defined

        return "Students(" + str(self.__students)  + ")"

    def __len__(self):
        """ returns a  """

        return len(self.__students)


studenten_uni_musterstadt = UniversityRegister()

studenten_uni_musterstadt.add_student("Kloth")
studenten_uni_musterstadt.add_student("Andresen")
studenten_uni_musterstadt.add_student("Drehwitz")

studenten_uni_musterstadt.increase_student_term("Kloth")

print(studenten_uni_musterstadt.get_student_term("Drehwitz"))

# #### SPECIAL METHODS CALLS ####
print( repr(studenten_uni_musterstadt) ) # equivalent to __repr__()
print( studenten_uni_musterstadt ) # equivalent str(xyz) -> equivalent to __str__()
print( len(studenten_uni_musterstadt) ) # hooked to __len__()
