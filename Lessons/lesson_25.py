import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# read data
heart_rate = []
with open('Lessons/health.csv', 'r') as f:
    header = f.readline()
    data = f.readlines()

time = []
t = 0
for line in data:
    s1, s2, s3 = line.strip().split(',')
    heart_rate.append([int(s1), int(s2), int(s3)])
    time.append(t)
    t += 1

# statistics
mean  = []
std   = []
min_hr = []
max_hr = []

for v in heart_rate:
    mean.append(np.mean(v))
    std.append(np.std(v))
    min_hr.append(np.min(v))
    max_hr.append(np.max(v))

print('Mean: ', mean)
print('Std: ', std)

# plot
plt.errorbar(time, mean, yerr=std, fmt='o', color='#023047')
plt.xlabel('Time (hours)')
plt.ylabel('Heart Rate (bpm)')
plt.fill_between(time, max_hr, min_hr, alpha=0.5, color='blue', linewidth=0.0)
plt.title('Heart Rate')
plt.show()

# quiz
sensorA = [16, 24, 24, 9, 23, 26, 26, 23, 25, 14]  
sensorB = [2, 19, 25, 10, 11, 24, 17, 7, 24, 17]  
sensorC = [15, 11, 24, 21, 6, 2, 18, 27, 1, 16]

mean = [np.mean(sensorA), np.mean(sensorB), np.mean(sensorC)]
std  = [np.std(sensorA), np.std(sensorB), np.std(sensorC)]

plt.errorbar(["A","B","C"], mean, yerr=std, fmt='o', color='#023047')
plt.xlabel('Sensor')
plt.ylabel('Temperature (C)')
plt.title('Temperature')
plt.show()

