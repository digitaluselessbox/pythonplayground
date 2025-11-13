class Cube():

    def __init__(self, side_length):
        self.__side_length = side_length

    def getSideLength(self):
        return self.__side_length

    def volume(self):
        return self.__side_length ** 3

    def surface(self):
        return self.__side_length ** 2 * 6


# danach erzeugen wir eine Instanz deiner Cube-Klasse
a = Cube(3)

print(a.getSideLength())

print(a.volume())

print(a.surface())
