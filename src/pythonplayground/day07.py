# OOP in Python:


# Wir definieren die Klasse Student mit der Methode name(),
# Klassennamen beginnen gemäß Konvention mit Großbuchstaben

# Wir definieren die Klasse Student mit der Methode name(), Klassennamen beginnen gemäß Konvention mit Großbuchstaben

class Student:
    def name(self):
        print(self.firstname + " " + self.lastname)

# Objekt erzeugen
s = Student()
s.firstname = "Anna"
s.lastname = "Müller"

# Methode aufrufen
# intern passiert quasi folgendes: Student.name(s)
s.name()

# self ist eine Referenz auf das aktuelle Objekt, also die Instanz der Klasse selbst.



# mit Constructor

class Employee:
    '''employee Class'''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        ''' methode prints the complete name of the employee '''
        print(self.firstname + " " + self.lastname)

s = Employee("Anna", "Müller")
s.name()  # -> Anna Müller



class StudentFinal():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        # Hier initialisieren wir die neue Variable term (Eigenschaft)
        self.term = 1

    def increase_term(self):
        """ Mit dieser Methode erhöhen wir die Variable term um 1 """
        self.term = self.term + 1

    def name(self):
        """ name() gibt nunmehr zusätzlich die Anzahl der Semester aus """
        print(self.firstname + " " + self.lastname + " (Semester: " + str(self.term) + ")")


erik = StudentFinal("Erik", "Mustermann")
erik.increase_term()
erik.name()
