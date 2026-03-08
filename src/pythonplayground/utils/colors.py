"""
Utility functions for color manipulation, such as darkening and lightening
colors. These functions can be used to create variations of colors for
different purposes, such as highlighting or shading elements in a graphical
application like a solar system visualization. ;)
"""

def darken_color(color, factor=0.5):
    """
        Darken a color by multiplying its RGB components by a factor.
        The factor should be between 0 and 1.
        0: completely black; 1: the original color
    """
    r, g, b = color

    return (
        int(r * factor),
        int(g * factor),
        int(b * factor),
    )

def lighten_color(color, factor=0.5):
    """
        Lighten a color by adding a fraction of the difference between the color and white to the original color.
        The factor should be between 0 and 1.
        0: the original color; 1: completely white
    """
    r, g, b = color

    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)

    return (r, g, b)
