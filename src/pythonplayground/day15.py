"""no module at all. Just testing a sphere class."""

import math


class Sphere:
    """represent a geometric sphere"""

    def __init__(self, radius) -> None:
        self.radius = radius

    def get_radius(self) -> int:
        """Return the radius of the sphere"""
        return self.radius

    def diameter(self) -> int:
        """Calculate and return the diameter of the Sphere"""
        return self.get_radius() * 2

    def volume(self) -> float:
        """Calculate and return the volume of the sphere"""
        return 4 / 3 * math.pi * self.get_radius() ** 3

    def surface(self) -> float:
        """Calculate and return the surface of the sphere"""
        return (self.get_radius() * 2) ** 2 * math.pi


my_sphere = Sphere(4)

# 4
print(my_sphere.get_radius())

# 8
print(my_sphere.diameter())

# 268.082573106329
print(my_sphere.volume())

# 201.06192982974676
print(my_sphere.surface())
