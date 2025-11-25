
# import version 1 - full namespace
import matplotlib.pyplot
from matplotlib import pyplot

matplotlib.pyplot.plot([1,2,3],[5,4,5])
matplotlib.pyplot.show()

# import version 2 only - import to modul object namespace
from matplotlib import pyplot

pyplot.plot([1,2,3],[5,4,5])
pyplot.show()

# import version 3 - import modul object with own name
import matplotlib.pyplot as plt # ←←← recommended best practice version
# from matplotlib import pyplot as plt

plt.plot([1,2,3],[5,4,5])
plt.show()
