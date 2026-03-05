# Instructions:
# create a simple solar system using the turtle module.

# Optional: Add moons orbiting the planets, using even smaller circles.
# Optional: Include labels for the Sun, planets, and moons using the turtle's write()

# from turtle import Screen, Turtle, done
import turtle
from solar_system import Planet

LINE_COLOR_DEFAULT = (0, 0, 0)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

planets = [
    {"name": "Sun", "radius": 60, "x": 0, "color": (255, 204, 0), "show_orbit": True},

    {"name": "Mercury", "radius": 3, "x": 420, "color": (169, 169, 169), "show_orbit": True},
    {"name": "Venus",   "radius": 5, "x": 650, "color": (218, 165, 32), "show_orbit": True},
    {"name": "Earth",   "radius": 6, "x": 780, "color": (70, 130, 180), "show_orbit": True},
    {"name": "Mars",    "radius": 4, "x": 980, "color": (188, 39, 50), "show_orbit": True},

    {"name": "Jupiter", "radius": 20, "x": 1300, "color": (210, 180, 140), "show_orbit": True},
    {"name": "Saturn",  "radius": 18, "x": 1500, "color": (222, 184, 135), "show_orbit": True},
    {"name": "Uranus",  "radius": 10, "x": 1680, "color": (175, 238, 238), "show_orbit": True},
    {"name": "Neptune", "radius": 10, "x": 1820, "color": (72, 61, 139), "show_orbit": True},
]

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.colormode(255)
screen.bgcolor("black")  # Set the background color

pen = turtle.Turtle()

# Set up the turtle
pen.speed(5)  # Set the speed of the turtle


def calculate_planet_coordinates(screen_w, planet_data):
    # we want to draw the planets from left to right, starting from left
    # the planet should be in one line with the center of the screen
    #
    # x: based on the planet radius, we can calculate the x position of the planet on the screen.
    # y: with the planet radius, we can calculate the y position of the planet on the screen.

    return -screen_w // 2 + planet_data["x"], -planet_data["radius"]


for planet in planets:

    positions = calculate_planet_coordinates(SCREEN_WIDTH, planet)
    #print(positions)

    planet_obj = Planet(planet, positions, pen)

    planet_obj.draw_planet() # Draw the planet
    planet_obj.draw_label() # Draw the label of the planet
    planet_obj.draw_orbit() # Draw the ecliptic plane of the planet


turtle.done()
