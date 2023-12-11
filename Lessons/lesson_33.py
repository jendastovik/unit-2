from matplotlib import pyplot as plt
plt.style.use("ggplot")
hyperbole1 = []
yaxes = []
for x in range(-200, 200, 4):
    hyperbole1.append((x/100)**2)
    yaxes.append(x/100)

hyperbole2 = [-x for x in hyperbole1]


plt.plot(hyperbole1, yaxes, color="red")
plt.plot(hyperbole2, yaxes, color="black")
plt.plot(yaxes, hyperbole1, color="blue")
plt.plot(yaxes, hyperbole2, color="green")

plt.legend(["y = x^2", "y = -x^2", "x = y^2", "x = -y^2"])
plt.show()

