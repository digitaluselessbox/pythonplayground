""" no module at all. Just testing a cube class. """
class Cube():
    """ a class represent a cube """

    def __init__(self, side_length):
        self.__side_length = side_length

    def get_side_length(self) -> int:
        """ return the side length of the cube """
        return self.__side_length

    def volume(self) -> int:
        """ return the volume of the cude """
        return self.get_side_length() ** 3

    def surface(self) -> int:
        """ return the surface of the cude """
        return self.get_side_length() ** 2 * 6


my_cube = Cube(3)

# 3
print(my_cube.get_side_length())

# 27
print(my_cube.volume())

# 54
print(my_cube.surface())
