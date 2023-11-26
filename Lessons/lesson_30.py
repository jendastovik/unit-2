# quiz
import requests
import matplotlib.pyplot as plt
from unit2_lib import get_sensor, smoothing


sensor = get_sensor(id=2)
t, val = smoothing(sensor, smoothing_win=5, overlap=1)

# get data from 200 to 400
y = []
x = []

for i in range(len(val)):
    if t[i] > 200 and t[i] < 400:
        y.append(val[i])
        x.append(t[i])


# create model
import numpy as np

# linear model
linear = np.polyfit(x, y, 1)
plt.subplot(2, 1, 1)
plt.plot(x, y, color="red")
plt.plot(x, np.polyval(linear, x), color="blue")
plt.title(f"Linear model: {linear[0]:.2f}x + {linear[1]:.2f}")

# quadratic model
quad = np.polyfit(x, y, 2)
plt.subplot(2, 1, 2)
plt.plot(x, y, color="red")
plt.plot(x, np.polyval(quad, x), color="blue")
plt.title(f"Quadratic model: {quad[0]: .2e}x^2 + {quad[1]:.2f}x + {quad[2]:.2f}")
plt.show()

# project
