""" used by day33_tourtle_solarsystem.py to represent a planet in the solar system """

from turtle import Turtle

class Planet:
    """ A class representing a planet in the solar system. It contains methods to draw the planet, its label and its orbit on the screen using turtle graphics. """
    def __init__(self, planet_data:dict, coordinates:tuple, pen_obj:Turtle):
        self.name = planet_data["name"]
        self.radius = planet_data["radius"]
        self.orbit_radius = planet_data["x"]
        self.color = planet_data["color"]
        self.show_orbit = planet_data["show_orbit"]
        self.pos_x = coordinates[0]
        self.pos_y = coordinates[1]
        self.pen = pen_obj


    def move_pen_to(self, position):
        """ Move the pen to the given position without drawing. """
        self.pen.penup()
        self.pen.goto(position[0], position[1])
        self.pen.pendown()

    def set_colors(self):
        """ Set the pen color and fill color to the planet's color. """
        self.pen.color(self.color, self.color)

    def draw_planet(self):
        """ Draw the planet on the screen at its position with its radius and color. """
        self.move_pen_to((self.pos_x, self.pos_y))
        self.set_colors()

        self.pen.begin_fill()
        self.pen.circle(self.radius)
        self.pen.end_fill()

    def draw_label(self):
        """ Draw the label of the planet on the screen. """
        self.move_pen_to((self.pos_x + len(self.name) * 5, self.pos_y - 20))
        self.pen.color("white")
        self.pen.write(self.name, align="center", font=("Arial", 11, "normal"))

    def draw_orbit(self):
        """ Draw the orbit of the planet on the screen. """
        if self.show_orbit:
            self.pen.speed(15)  # Increase speed for drawing the planet's orbit

            #move to the center of the solar system to draw the orbit of the planet
            self.move_pen_to((self.pos_x - self.orbit_radius, -self.orbit_radius))

            self.pen.color(self.color)
            self.pen.circle(self.orbit_radius)  # Draw the orbit of the planet

            self.move_pen_to((self.pos_x, self.pos_y)) # Move back to the planet's position
            self.pen.speed(5) # Reset speed for drawing
