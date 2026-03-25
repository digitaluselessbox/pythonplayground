# Instructions:
# create a dynamic moving solar system using the turtle module.
# The planets should orbit around the sun, and the moons should orbit around their respective planets.
#
# deliniation of the solar system:
# - the sun is in the center of the screen and does not move
# - the many moons of Jupiter, Saturn are not drawn as individual circles, but instead the number of moons is written next to the planet's name


import json
import turtle
import solar_system_v2 as solar_system


creator = turtle.Turtle()
galaxy = solar_system.Galaxy(creator, width=1080, height=1080)
planets = []

moveable_objects = []

# check if the planets.json file exists in the expected location
try:
    with open("solar_system_v2/planets.json", "r", encoding="utf-8") as file:

        planets = json.load(file)["planets"]

        galaxy.draw_background_stars(num_stars=200) # Draw the galaxy background with stars

        for planet_data in planets:

            planet = solar_system.Planet(planet_data, galaxy)
            moveable_objects.append(planet) # add the planet to the list of moveable objects

            # todo: how to create dynamic object names and call them by name from the json file?

            # planet.draw_orbit() # Draw the ecliptic plane of the planet
            # planet.draw_planet() # Draw the planet
            # planet.draw_label() # Draw the label of the planet
            # planet.draw_moons() # Draw the moons of the planet

            # todo: add moons to the planets, and make them move around the planets in their own orbits

    # todo: while loop to move the planets in their orbits

    print(moveable_objects)

except FileNotFoundError:
    # draw error message on the screen using turtle
    creator.color("red")
    creator.write("Error: No planet data found. No planets, no galaxy, nothing!!!", align="center", font=("Arial", 16, "bold"))


turtle.done()
