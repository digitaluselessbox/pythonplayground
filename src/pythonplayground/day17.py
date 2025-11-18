"""testing code imports"""

# import version 1 - complete module
import day17_hello

print(day17_hello)

day17_hello.world()
day17_hello.mars()


# import version 2 - import only function
from day17_hello import world, mars

world()
mars()


# import version 3 - import all functions with wildcard
# (no best practice, be specific!!!)
from day17_hello import *

world()
mars()
