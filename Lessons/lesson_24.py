import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
temp = [1.5, 1.5, 2.0, 2.8, 3.2, 4.0, 5.0, 5.0, 6.0]
time = [t*5 for t in range(len(temp))]
plt.scatter(time, temp, color="blue")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (C)")

m, b = np.polyfit(time, temp, 1)
print(f"Linear model T(t) = {m:.2f}t + {b:.2f}")
time_model = [t*5 for t in range(len(temp))]
temp_model = [m*t + b for t in time_model]

plt.plot(time_model, temp_model, color="black")
plt.text(1, 4, f"Linear model T(t) = {m:.2f}t + {b:.2f}", fontsize=20)
plt.show()

temp_future = m*45 + b
print(f"Prediction linear model {temp_future:.2f} C = {m:.2f}(45min) + {b:.2f}")

#quiz
h = [57,56,57,56,55,55,54,54,54,53,53,54,53,53,52,52,51,51,51,50,50,49,50,49,49,48,49,49,48,48,48,49]
t = [t*10 for t in range(len(h))]

m,b = np.polyfit(t,h,1)
print(f"Linear model h(t) = {m:.2f}t + {b:.2f}")
plt.scatter(t,h, color="blue")
plt.xlabel("Time (min)")
plt.ylabel("Humdiity (%)")
t_model = [t*10 for t in range(len(h))]
h_model = [m*t + b for t in t_model]
plt.plot(t_model, h_model, color="black")
plt.show()



