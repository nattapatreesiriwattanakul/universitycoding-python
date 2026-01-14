# 6610742246 Nattapat Reesiriwattanakul
# lab8 Question C
# matplot และกำหนดค่าx y ตามโจทย์ อย่าลืมplt.show()ด้วย

import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(5, 20)
y = np.exp(x / 3.0)

f = interpolate.interp1d(x, y)

x1 = np.arange(6, 12)
y1 = f(x1)  # use interpolation function returned by `interp1d`

plt.plot(x, y, 'o', x1, y1, '--')
plt.show()
