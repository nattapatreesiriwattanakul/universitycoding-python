# 6610742246 Nattapat Reesiriwattanakul
# lab8 Question A
# import numpy and pypplot for anable program

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 7

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()
