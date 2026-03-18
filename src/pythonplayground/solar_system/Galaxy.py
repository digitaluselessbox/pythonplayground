""" used by day33_tourtle_solarsystem.py to represent the galaxy """

import turtle
import random
from contextlib import contextmanager

class Galaxy:
    """ A class representing the galaxy in which the solar system is located. """

    def __init__(self, pen_obj:turtle.Turtle, width=1920, height=1080):
        """ Initialize the galaxy with a turtle pen object and the dimensions of the galaxy. """
        self.pen = pen_obj
        self.galaxy_width = width
        self.galaxy_height = height

        self.galaxy = turtle.Screen()
        self.galaxy.setup(width=self.galaxy_width, height=self.galaxy_height)
        self.galaxy.colormode(255)
        self.galaxy.bgcolor("black")  # Set the background color
        self._tracer_value = 1
        self._tracer_delay = None

        print(self.galaxy.tracer()) # Check the current tracer settings

        # Set up the turtle
        self.pen.speed(0)  # Set the speed of the turtle
        self.pen.hideturtle() # Hide the turtle cursor while drawing

    def draw_background_stars(self, num_stars=100):
        """ Draw random stars in the background of the solar system. """
        self.pen.color("white")
        self.pen.shape("circle")
        self.pen.shapesize(0.05, 0.05, 0)  # Set the size of the turtle shape for stars

        with self.temporary_tracer(0):
            for _ in range(num_stars):
                x = random.randint(-self.galaxy_width // 2, self.galaxy_width // 2)
                y = random.randint(-self.galaxy_height // 2, self.galaxy_height // 2)

                self.pen.teleport(x, y)
                self.pen.stamp()


    def calculate_planet_position(self, planet_data):
        """Calculate the drawing position for a planet based on input data."""

        # we want to draw the planets from left to right, starting from left
        # the planet should be in one line with the center of the screen
        #
        # x: based on the planet radius, we can calculate the x position of the planet on the screen.
        # y: with the planet radius, we can calculate the y position of the planet on the screen.

        return -self.galaxy_width // 2 + planet_data["x"], -planet_data["radius"]


    def set_draw_tracer(self, value:int, delay: int | None = None):
        """Set tracer settings for the galaxy screen."""
        if delay is None:
            self.galaxy.tracer(value)
        else:
            self.galaxy.tracer(value, delay)
        self._tracer_value = value
        self._tracer_delay = delay

    # A context manager to temporarily set tracer settings and restore previous values afterwards.
    # It is the same logic as with opening a file with "with open() as f:" and automatically closing the file after the block of code is executed.
    @contextmanager
    def temporary_tracer(self, value: int, delay: int | None = None):
        """Temporarily set tracer settings and restore previous values afterwards."""
        previous_n = self._tracer_value
        previous_delay = self._tracer_delay
        self.set_draw_tracer(value, delay)
        try:
            yield
        finally:
            self.set_draw_tracer(previous_n, previous_delay)
