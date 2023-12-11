#quiz
from unit2_lib import get_sensor, smoothing
import matplotlib.pyplot as plt


sensor1 = get_sensor(id=1)
sensor2 = get_sensor(id=2)

sum = [a + b for a, b in zip(sensor1, sensor2)]
sum = smoothing(sum, smoothing_win=5, overlap=1)[1]

avg = [(a+b)/2 for a, b in zip(sensor1, sensor2)]
avg = smoothing(avg, smoothing_win=5, overlap=1)[1]

plt.subplot(4, 1, 1)
plt.plot(sensor1, color="red")
plt.subplot(4, 1, 2)
plt.plot(sensor2, color="blue")
plt.subplot(4, 1, 3)
plt.plot(sum, color="green")
plt.subplot(4, 1, 4)
plt.plot(avg, color="orange")
plt.show()


# project
plt.style.use("ggplot")

sensors = []

for s in [1, 2 , 3]:
    sensors.append(get_sensor(id=s))
    print(f"Sensor {s} has {len(sensors[s-1])} samples")

num_samples = len(sensors[0])

# average of all sensors except sensor 0
avg =[]
for i in range(num_samples):
    tot = 0
    for s in sensors:
        tot += s[i]
    avg.append(tot/len(sensors))

fig = plt.figure(figsize=(10, 8))
grid = plt.GridSpec(3, 3, figure=fig)
plt.subplots_adjust(hspace=0.5)

box1 = fig.add_subplot(grid[0:2, 0:2])
plt.plot(avg, color="red")
plt.title("Average of all sensors")

box2 = fig.add_subplot(grid[0,2])
plt.plot(get_sensor(id=0), color="blue")
plt.title("Sensor id=0")

box3 = fig.add_subplot(grid[1,2])
plt.plot(sensors[0], color="green")
plt.title("Sensor id=1")

box4 = fig.add_subplot(grid[2,0])
plt.plot(sensors[1], color="orange")
plt.title("Sensor id=2")

box5 = fig.add_subplot(grid[2,1])
plt.plot(sensors[2], color="purple")
plt.title("Sensor id=3")


plt.show()