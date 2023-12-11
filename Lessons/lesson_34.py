import matplotlib.pyplot as plt
import numpy as np

# quiz
plt.style.use("ggplot")

parabola1 = [(x/100+2)**2 for x in range(-600, 0, 4)]
parabola2 = [(x/100-2)**2 for x in range(0, 600, 4)]
yaxes1 = [x/100 for x in range(-600, 0, 4)]
yaxes2 = [x/100 for x in range(0, 600, 4)]
parabola3 = [-x for x in parabola1]
parabola4 = [-x for x in parabola2]


plt.plot(yaxes1, parabola1, color="blue")
plt.plot(yaxes2, parabola2, color="green")
plt.plot(yaxes1, parabola3, color="red")
plt.plot(yaxes2, parabola4, color="black")

plt.legend(["y = (x+2)^2", "y = (x-2)^2", "y = -(x+2)^2", "y = -(x-2)^2"])
plt.xlim(-15, 15)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
