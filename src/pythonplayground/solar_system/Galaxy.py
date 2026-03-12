""" used by day33_tourtle_solarsystem.py to represent the galaxy """

import turtle
import random

class Galaxy:
    """ A class representing the galaxy in which the solar system is located. """

    def __init__(self, pen_obj:turtle.Turtle, width=1920, height=1080):
        """ Initialize the galaxy with a turtle pen object and the dimensions of the galaxy. """
        self.pen = pen_obj
        self.galaxy_width = width
        self.galaxy_height = height

        galaxy = turtle.Screen()
        galaxy.setup(width=self.galaxy_width, height=self.galaxy_height)
        galaxy.colormode(255)
        galaxy.bgcolor("black")  # Set the background color

        # Set up the turtle
        self.pen.speed(0)  # Set the speed of the turtle
        self.pen.hideturtle() # Hide the turtle cursor while drawing

    def draw_background_stars(self, num_stars=100):
        """ Draw random stars in the background of the solar system. """
        self.pen.color("white")
        self.pen.shape("circle")
        self.pen.shapesize(0.05, 0.05, 0)  # Set the size of the turtle shape for stars

        for _ in range(num_stars):
            x = random.randint(-self.galaxy_width // 2, self.galaxy_width // 2)
            y = random.randint(-self.galaxy_height // 2, self.galaxy_height // 2)

            self.pen.teleport(x, y)
            self.pen.stamp()


    def calculate_planet_coordinates(self, planet_data):
        """ Calculate the coordinates of the planet """

        # we want to draw the planets from left to right, starting from left
        # the planet should be in one line with the center of the screen
        #
        # x: based on the planet radius, we can calculate the x position of the planet on the screen.
        # y: with the planet radius, we can calculate the y position of the planet on the screen.

        return -self.galaxy_width // 2 + planet_data["x"], -planet_data["radius"]
