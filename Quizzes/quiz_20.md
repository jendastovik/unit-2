# Quiz 20
## Python code
```python
import random
random.seed(1234)
def procedure(n, m, s):
    out = "/    x   /   y(x)  /"
    for _ in range(n):
        x = random.randint(0, 100)
        yx = x*0.5*(m/s)**2
        out += f"\n/{str(x).center(8)}/ {str(yx).center(8)}/"
    return out
```

## Output
![](/assets/qx.png)
