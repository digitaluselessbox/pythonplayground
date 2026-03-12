""" used by day33_tourtle_solarsystem.py to represent a planet in the solar system """

import turtle
import utils.colors as color_utils

class Planet:
    """ A class representing a planet in the solar system. It contains methods to draw the planet, its label and its orbit on the screen using turtle graphics. """
    def __init__(self, planet_data:dict, coordinates:tuple, pen_obj:turtle.Turtle):
        self.name = planet_data.get("name", "Unknown Planet")
        self.radius = planet_data.get("radius", 10)
        self.orbit_radius = planet_data.get("x", 0)

        # Accept both hex ("#RRGGBB") and RGB strings ("(r, g, b)" / "r,g,b").
        color_value = str(planet_data.get("color", "#FFFFFF"))
        self.color:color_utils.RGBColor = color_utils.parse_color(color_value)

        self.show_orbit = planet_data.get("show_orbit", False)
        self.moons = planet_data.get("moons", 0)
        self.pos_x = coordinates[0]
        self.pos_y = coordinates[1]
        self.pen = pen_obj


    def move_pen_to(self, position):
        """ Move the pen to the given position without drawing. """
        # self.pen.penup()
        # self.pen.goto(position[0], position[1])
        # self.pen.pendown()
        self.pen.teleport(position[0], position[1])

    def set_colors(self, line_color: color_utils.RGBColor | None = None, fill_color: color_utils.RGBColor | None = None):
        """ Set the pen color and fill color to the planet's color. """
        if line_color is None:
            line_color = self.color
        if fill_color is None:
            fill_color = self.color
        self.pen.color(line_color, fill_color)

    def draw_planet(self):
        """ Draw the planet on the screen at its position with its radius and color. """
        self.move_pen_to((self.pos_x, self.pos_y))

        self.pen.pensize(2)
        self.set_colors( line_color=color_utils.darken_color(self.color, 0.4), fill_color=self.color)

        self.pen.begin_fill()
        self.pen.circle(self.radius)
        self.pen.end_fill()

        self.pen.pensize(1)

    def draw_label(self):
        """ Draw the label of the planet on the screen. """
        self.move_pen_to((self.pos_x + len(self.name) * 2, self.pos_y - 20))
        self.pen.color("white")
        self.pen.write(self.name, align="left", font=("Arial", 11, "normal"))

    def draw_orbit(self):
        """ Draw the orbit of the planet on the screen. """
        if self.show_orbit and self.orbit_radius > 0:
            self.pen.speed(15)  # Increase speed for drawing the planet's orbit

            #move to the center of the solar system to draw the orbit of the planet
            self.move_pen_to((self.pos_x - self.orbit_radius, -self.orbit_radius))

            self.pen.color(color_utils.darken_color(self.color, 0.4)) # Set the color of the orbit to a darker shade of the planet's color
            self.pen.circle(self.orbit_radius)  # Draw the orbit of the planet

            self.move_pen_to((self.pos_x, self.pos_y)) # Move back to the planet's position
            self.pen.speed(5) # Reset speed for drawing

    def draw_moons(self):
        """Draw small dots representing moons below the planet."""

        max_display_row = 10

        start_x = self.pos_x + len(self.name) * 2 + 10
        start_y = self.pos_y - 60

        if self.moons > 0:
            # Write the number of moons next to the planet's name
            self.move_pen_to((start_x, start_y + 10))
            self.pen.color("white")
            self.pen.write(f"{self.moons} moon{'s' if self.moons > 1 else ''}", align="left", font=("Arial", 11, "normal"))
            start_y -= 10 # Move down for the moon dots

        self.pen.shape("circle")
        self.pen.shapesize(0.3, 0.3)  # Set the size of the turtle shape
        self.pen.color("#383838")  # Set the color for the moons

        for i in range(self.moons):
            row = i // max_display_row
            col = i % max_display_row

            x = start_x + col * 9
            y = start_y - row * 9

            self.move_pen_to((x, y))
            self.pen.stamp()
