# Quiz 23
## Python code
```python
import matplotlib.pyplot as plt

Ys = [abs(x/10) for x in range(-100, 100, 2)]
Xs = [x/10 for x in range(-100, 100, 2)]

plt.style.use('ggplot')
plt.plot(Xs, Ys)
plt.xlabel("X")
yLabel = "f(x): |x|"
plt.ylabel(yLabel)
plt.show()
```

## Output
![](/assets/q23.png)

## B part
![](/assets/bpart/q23.png)
