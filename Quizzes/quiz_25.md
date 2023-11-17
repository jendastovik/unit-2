# Quiz 25
## Python code
```python
import matplotlib.pyplot as plt
import numpy as np

sensorA = [16, 24, 24, 9, 23, 26, 26, 23, 25, 14]  
sensorB = [2, 19, 25, 10, 11, 24, 17, 7, 24, 17]  
sensorC = [15, 11, 24, 21, 6, 2, 18, 27, 1, 16]

mean = [np.mean(sensorA), np.mean(sensorB), np.mean(sensorC)]
std  = [np.std(sensorA), np.std(sensorB), np.std(sensorC)]

plt.style.use('ggplot')
plt.errorbar(["A","B","C"], mean, yerr=std, fmt='o', color='#023047')
plt.xlabel('Sensor')
plt.ylabel('Temperature (C)')
plt.title('Temperature Readings for 3 Sensors')
plt.show()
```

## Output
![](/assets/q25.png)

