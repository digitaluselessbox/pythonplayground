 # Instructions:

# Using filled shapes, draw a simple house. Your house should have at least:

# A square or rectangle for the main building.
# A triangle for the roof.
# At least one window or door, using any shape.
# Feel free to add additional details like a chimney, pathway, or surrounding trees using shapes and colors.

# Tips:

# Use begin_fill() and end_fill() to fill in each shape.
# Change colors between shapes to make your house more vibrant.
# Use penup() and pendown() to move between different parts of your drawing without drawing lines.

from turtle import *

bgcolor("lightblue")  # Set the background color

# Set up the turtle
speed(5)  # Set the speed of the turtle
color("black", "white")  # Set pen color and fill color

LINE_COLOR_DEFAULT = "black"


# command pattern implementation for better readability and less code repetition
# instead of calling begin_fill() and end_fill() in every shape drawing function,
# we can use a helper function that takes care of the filling process.
# This way, we can focus on the actual drawing commands for each shape,
# making the code cleaner and more maintainable.
def draw_filled_steps(steps):
    begin_fill()
    for action, args in steps:
        action(*args)
    end_fill()


def set_colors(line_color=LINE_COLOR_DEFAULT, fill_color=None):
    color_args = [line_color]
    if fill_color:
        color_args.append(fill_color)
    color(*color_args)


def move_pen_tip(x:int, y:int):
    penup()
    goto(x, y)
    pendown()


def draw_circle(radius, line_color=LINE_COLOR_DEFAULT, fill_color=None):
    set_colors(line_color, fill_color)

    draw_filled_steps([
        (circle, (radius,)),
    ])


def draw_square(size, line_color=LINE_COLOR_DEFAULT, fill_color=None):
    set_colors(line_color, fill_color)

    # here we use a list as the args for the forward and right functions.
    # It is much more readable than writing Touple style (size,) and (90,).
    # compare with draw_triangle function below, where we use Touple style.
    draw_filled_steps([
        (forward, [size]),
        (right, [90]),
    ] * 4)


def draw_triangle(size, degree, line_color=LINE_COLOR_DEFAULT, fill_color=None):
    set_colors(line_color, fill_color)

    # here we use Touple style for the args, which is also valid, but less readable.
    # but you have the unchangeable semantic of a Tuple, which is not the case for a list.
    # compare with draw_square function above.
    draw_filled_steps([
        (forward, (size,)),
        (right, (degree,)),
    ] * 3)


def draw_rectangle(width, height, line_color=LINE_COLOR_DEFAULT, fill_color=None):
    set_colors(line_color, fill_color)

    draw_filled_steps([
        (forward, (width,)),
        (right, (90,)),
        (forward, (height,)),
        (right, (90,)),
    ] * 2)


# Draw the main building
move_pen_tip(0, 0)  # Move to the starting position
draw_rectangle(300, 200, "#000000", "#b12929")

# Draw the roof
move_pen_tip(-30, 0)  # Move to the top of the building
draw_triangle(360, -120, "#353d35")

# Draw the door
move_pen_tip(50, -30)  # Move to the position for the door
draw_rectangle(80, 170, "#000000", "#C5905B")

# Draw a window
move_pen_tip(150, -50)  # Move to the position for the window
draw_rectangle(100, 60, "#000000", "#3088D0")

# draw another round window in the roof
move_pen_tip(150, 100)  # Move to the position for the round window
draw_circle(40, "#000000", "#3088D0")


done()
