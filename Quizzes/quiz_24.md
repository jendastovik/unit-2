# Quiz 24
## Python code
```python
import matplotlib.pyplot as plt
import numpy as np

h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]
t = [t*10 for t in range(len(h))]

m,b = np.polyfit(t,h,1)
print(f"Linear model h(t) = {m:.2f}t + {b:.2f}")

plt.style.use('ggplot')
plt.scatter(t,h, color="blue")
plt.xlabel("Time (min)")
plt.ylabel("Humdity (%)")
plt.title(f"Linear model h(t) = {m:.2f}t + {b:.2f}")
t_model = [t*10 for t in range(len(h))]
h_model = [m*t + b for t in t_model]
plt.plot(t_model, h_model, color="black")
plt.show()
```

## Output
![](/assets/q24.png)

## B part
![](/assets/bpart/q24.png)