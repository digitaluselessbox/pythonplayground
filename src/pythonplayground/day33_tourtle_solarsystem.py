# Instructions:
# create a simple solar system using the turtle module.

# Optional: Add moons orbiting the planets, using even smaller circles.
# Optional: Include labels for the Sun, planets, and moons using the turtle's write()


import json
import time
import turtle
import solar_system


def wait_for_start(screen, pen: turtle.Turtle) -> None:
    """Wait for user input in the turtle window before drawing starts."""
    started = False

    def start(*_args):
        nonlocal started
        started = True

    pen.color("white")
    pen.teleport(0, 0)
    pen.write("Bereit für eine Reise durch das Sonnensystem?", align="center", font=("Arial", 40, "normal"))

    screen.listen()
    screen.onkey(start, "Return")
    screen.onkey(start, "KP_Enter")
    screen.onclick(start)

    while not started:
        screen.update()
        time.sleep(0.01)

    screen.onkey(None, "Return")
    screen.onkey(None, "KP_Enter")
    screen.onclick(None)
    pen.clear()


creator = turtle.Turtle()

galaxy = solar_system.Galaxy(creator, width=1920, height=1080)
wait_for_start(galaxy.galaxy, creator)
galaxy.draw_background_stars(num_stars=200) # Draw the galaxy background with stars

planets = []


# check if the planets.json file exists in the expected location
try:
    with open("solar_system/planets.json", "r", encoding="utf-8") as file:
        planets = json.load(file)["planets"]

        for planet_data in planets:

            planet = solar_system.Planet(planet_data, creator, galaxy)

            planet.draw_orbit() # Draw the ecliptic plane of the planet
            planet.draw_planet() # Draw the planet
            planet.draw_label() # Draw the label of the planet
            planet.draw_moons() # Draw the moons of the planet


except FileNotFoundError:
    # draw error message on the screen using turtle
    creator.color("red")
    creator.write("Error: No planet data found. No planets, no galaxy, nothing!!!", align="center", font=("Arial", 16, "bold"))


turtle.done()
