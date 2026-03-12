"""
Utility functions for color manipulation, such as darkening and lightening
colors. These functions can be used to create variations of colors for
different purposes, such as highlighting or shading elements in a graphical
application like a solar system visualization. ;)
"""

# Define a type alias for RGB color representation as a tuple of three int (r, g, b).
RGBColor = tuple[int, int, int]


def parse_color(color_value: str) -> RGBColor:
    """Parse a color string (#RRGGBB or r,g,b / (r, g, b)) into an RGB tuple."""
    color_value = color_value.strip()

    # handle hex color format
    if color_value.startswith("#") and len(color_value) == 7:
        r = int(color_value[1:3], 16)
        g = int(color_value[3:5], 16)
        b = int(color_value[5:7], 16)
        return int(r), int(g), int(b)

    # handle rgb color format "(r, g, b)" or "r, g, b"
    rgb_text = color_value.strip("()") # Remove parentheses if present
    parts = [part.strip() for part in rgb_text.split(",")] # Split by comma and strip whitespace

    if len(parts) == 3:
        r = int(parts[0])
        g = int(parts[1])
        b = int(parts[2])

        return int(r), int(g), int(b)

    return 255, 255, 255


def darken_color(color: RGBColor, factor: float = 0.5) -> RGBColor:
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


def lighten_color(color: RGBColor, factor: float = 0.5) -> RGBColor:
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
