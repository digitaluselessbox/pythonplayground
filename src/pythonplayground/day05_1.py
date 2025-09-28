# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

import math


def area_circle(radius: int) -> float:
    """returns the area on a circle with the given radius"""
    return math.pi * radius**2


def user_number_input(question: str) -> int:
    """Function asks user for a number input with a given question string."""

    number_input = ""

    while not number_input.isnumeric():
        number_input = input(f"{question}")

    return int( number_input )


def user_number_multiplication(question: str) -> int:
    """Function asks user for a number input with a given question string."""

    number_input = ""

    while not number_input.isnumeric():
        number_input = input(f"{question}")

    multiplicator = ""
    while not multiplicator.isnumeric():
        multiplicator = input("Bitte einen Multiplikator eingeben (Ganzzahl)!")

    return int(number_input) * int(multiplicator)
