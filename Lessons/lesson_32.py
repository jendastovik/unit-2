# quiz
from unit2_lib import *
import matplotlib.pyplot as plt

s4 = get_sensor(id=4)
s5 = get_sensor(id=5)
plt.style.use("ggplot")

fig = plt.figure(figsize=(10, 5))
grid = plt.GridSpec(3, 4, figure=fig)
plt.subplots_adjust(hspace=0.5)

box1 = fig.add_subplot(grid[1, 0])
plt.title("Sensor id=4")
plt.ylim(0, 100)
plt.xlim(0, 800)
plt.plot(s4, color="red")

box2 = fig.add_subplot(grid[1,3])
plt.title("Sensor id=5")
plt.ylim(0, 100)
plt.xlim(0, 800)
plt.plot(s5, color="blue")

subtraction = [(-a-b)/2 for a, b in zip(s4, s5)]
box3 = fig.add_subplot(grid[0:3, 1:3])
plt.title("(-sensror#4 - sensor#5)/2")
plt.plot(subtraction, color="green")

plt.subplots_adjust(wspace=0.24)

plt.show()